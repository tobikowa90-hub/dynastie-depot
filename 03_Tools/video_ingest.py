#!/usr/bin/env python3
"""Video ingest CLI: yt-dlp + whisper + quality gate + source-page stub.

Usage:
    python 03_Tools/video_ingest.py <youtube-url> --category <kategorie> \\
        --channel <channel-slug> --topic "<topic>" \\
        [--content-language en] [--note-language de] [--whisper-model large-v3]

Categories: earnings-calls | interviews | conferences | analyses | updating-system
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from video_ingest_lib import build_slug, sha256_file, quality_gate

VAULT = Path(__file__).resolve().parents[1] / "07_Obsidian Vault" / "Obsidian Mindmap" / "Investing Mastermind"
RAW_VIDEOS = VAULT / "raw" / "videos"
SRC_VIDEOS = VAULT / "wiki" / "sources" / "videos"


def tool_version(cmd: list[str]) -> str:
    """Return first line of `<tool> --version` output, or 'unknown'."""
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=10).stdout.strip()
        return out.split("\n", 1)[0] if out else "unknown"
    except Exception as e:
        return f"error: {e}"


def whisper_package_version() -> str:
    """Read openai-whisper version from package metadata (whisper has no --version)."""
    try:
        out = subprocess.run(
            [sys.executable, "-m", "pip", "show", "openai-whisper"],
            capture_output=True, text=True, timeout=10
        ).stdout
        for line in out.splitlines():
            if line.lower().startswith("version:"):
                return f"openai-whisper {line.split(':', 1)[1].strip()}"
        return "openai-whisper unknown"
    except Exception as e:
        return f"openai-whisper error: {e}"


def url_reachable(url: str, timeout: int = 10) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("url")
    p.add_argument("--category", required=True,
                   choices=["earnings-calls", "interviews", "conferences", "analyses", "updating-system"])
    p.add_argument("--channel", required=True, help="kebab-case channel slug, e.g. 'brk'")
    p.add_argument("--topic", required=True, help="short topic, e.g. 'annual qa'")
    p.add_argument("--upload-date", default=None, help="YYYY-MM-DD original upload (default: today)")
    p.add_argument("--content-language", default="en")
    p.add_argument("--note-language", default="de")
    p.add_argument("--whisper-model", default="large-v3")
    p.add_argument("--dry-run", action="store_true",
                   help="Skip whisper (large download), only do yt-dlp + stub")
    args = p.parse_args()

    upload_date = args.upload_date or date.today().isoformat()
    slug = build_slug(upload_date, args.channel, args.topic)
    work_dir = RAW_VIDEOS / args.category / slug
    if work_dir.exists():
        print(f"ERROR: {work_dir} already exists. Pick a different topic or add collision suffix.",
              file=sys.stderr)
        return 2
    work_dir.mkdir(parents=True)

    log_lines: list[str] = [f"# run.log for {slug}", f"started: {date.today().isoformat()}"]

    def log(msg: str) -> None:
        print(msg)
        log_lines.append(msg)

    def flush_log() -> None:
        """Always write run.log — call before every early exit."""
        try:
            (work_dir / "run.log").write_text("\n".join(log_lines), encoding="utf-8")
        except Exception as e:
            print(f"WARN: could not flush run.log: {e}", file=sys.stderr)

    # 0. URL reachability
    t0 = time.time()
    url_ok = url_reachable(args.url)
    log(f"[step 0] url_reachable={url_ok} ({time.time()-t0:.1f}s)")
    if not url_ok:
        log("FAIL: URL unreachable, abort")
        flush_log()
        return 3

    # Tool versions (pinned in run.log + later in frontmatter)
    versions = {
        "yt-dlp": tool_version(["yt-dlp", "--version"]),
        "whisper": whisper_package_version(),  # robust pkg-metadata lookup
        "ffmpeg": tool_version(["ffmpeg", "-version"]),
    }
    for k, v in versions.items():
        log(f"[version] {k}: {v}")

    # 1. yt-dlp download — single video only (--no-playlist)
    t0 = time.time()
    cmd = [
        "yt-dlp", "-x", "--audio-format", "m4a",
        "--no-playlist",                # critical: never download playlist by accident
        "--write-info-json",
        "-o", str(work_dir / "%(id)s.%(ext)s"),
        args.url,
    ]
    log(f"[step 1] yt-dlp: {' '.join(cmd)}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    log(f"[step 1] exit={r.returncode}, dt={time.time()-t0:.1f}s")
    if r.returncode != 0:
        log(f"FAIL: yt-dlp stderr:\n{r.stderr[-2000:]}")
        flush_log()
        return 4

    audio_files = list(work_dir.glob("*.m4a"))
    info_files = list(work_dir.glob("*.info.json"))
    if len(audio_files) != 1 or len(info_files) != 1:
        log(f"FAIL: expected exactly 1 audio + 1 info file, got "
            f"{len(audio_files)} audio + {len(info_files)} info; "
            f"dir contents: {[p.name for p in work_dir.iterdir()]}")
        flush_log()
        return 5

    audio = audio_files[0]
    info_path = info_files[0]
    info = json.loads(info_path.read_text(encoding="utf-8"))
    duration_sec = info.get("duration", 0)
    duration_min = duration_sec / 60 if duration_sec else 0
    chapters = info.get("chapters") or []
    chapters_path = None
    if chapters:
        chapters_path = work_dir / "chapters.json"
        chapters_path.write_text(json.dumps(chapters, indent=2), encoding="utf-8")

    # Rename info.json to canonical name
    info_canonical = work_dir / "info.json"
    info_path.rename(info_canonical)

    log(f"[info] duration_min={duration_min:.1f}, chapters={bool(chapters)}, video_id={info.get('id')}")

    # 2. whisper transcribe (skipped on dry-run)
    transcript_path = work_dir / "transcript.md"
    detected_lang = args.content_language
    segments = 0

    if args.dry_run:
        log("[step 2] DRY-RUN: skipping whisper, writing stub transcript")
        stub = (f"# Dry-run stub transcript for {slug}\n\n"
                f"[00:00:00] (whisper skipped via --dry-run)\n"
                + ("# pad\n" * 100))  # pad to >500 chars
        transcript_path.write_text(stub, encoding="utf-8")
        segments = 1
    else:
        t0 = time.time()
        # JSON output: stable language detection + segment timestamps in one file
        cmd = [
            "whisper", str(audio),
            "--model", args.whisper_model,
            "--language", args.content_language,
            "--output_format", "json",
            "--output_dir", str(work_dir),
        ]
        log(f"[step 2] whisper: {' '.join(cmd)}")
        r = subprocess.run(cmd, capture_output=True, text=True)
        log(f"[step 2] exit={r.returncode}, dt={time.time()-t0:.1f}s")
        if r.returncode != 0:
            log(f"FAIL: whisper stderr:\n{r.stderr[-2000:]}")
            flush_log()
            return 6

        whisper_json = work_dir / f"{audio.stem}.json"
        if not whisper_json.exists():
            log(f"FAIL: expected {whisper_json}, got {[p.name for p in work_dir.iterdir()]}")
            flush_log()
            return 7

        wjson = json.loads(whisper_json.read_text(encoding="utf-8"))
        detected_lang = (wjson.get("language") or args.content_language)[:2].lower()
        whisper_segments = wjson.get("segments", [])
        segments = len(whisper_segments)

        # Render segments as markdown with [HH:MM:SS] prefix for greppability
        def fmt_ts(seconds: float) -> str:
            h, rem = divmod(int(seconds), 3600)
            m, s = divmod(rem, 60)
            return f"[{h:02d}:{m:02d}:{s:02d}]"
        lines = [f"{fmt_ts(seg['start'])} {seg['text'].strip()}"
                 for seg in whisper_segments]
        transcript_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

        # Move raw whisper json to a stable name for audit (not deleted, small)
        whisper_json.rename(work_dir / "whisper_raw.json")

    # 3. Cleanup audio (Variante A)
    audio.unlink()
    log(f"[step 3] removed audio file {audio.name}")

    # 4. Hashes
    transcript_sha = sha256_file(transcript_path)
    info_sha = sha256_file(info_canonical)
    chapters_sha = sha256_file(chapters_path) if chapters_path else None
    log(f"[step 4] transcript_sha256={transcript_sha[:16]}..., info_sha256={info_sha[:16]}...")

    # 5. Quality gate
    transcript_text = transcript_path.read_text(encoding="utf-8")
    gate = quality_gate(
        transcript_text=transcript_text,
        duration_min=duration_min,
        segments=segments,
        detected_lang=detected_lang,
        expected_lang=args.content_language,
        url_ok=True,
    )
    log(f"[step 5] quality_gate: passed={gate.passed}, fails={gate.fails}, warns={gate.warns}")
    if not gate.passed:
        log("FAIL: quality gate failed, aborting before source-page write")
        flush_log()
        return 8

    # 6. run.log
    flush_log()

    # 7. Source-page stub
    src_dir = SRC_VIDEOS / args.category
    src_dir.mkdir(parents=True, exist_ok=True)
    src_page = src_dir / f"{slug}.md"

    fm = f"""---
title: "{info.get('title', slug)}"
type: source
medium: video
tags: []
created: {date.today().isoformat()}
updated: {date.today().isoformat()}
sources: [{slug}]
related: []

video:
  platform: youtube
  video_id: "{info.get('id', '')}"
  source_url: "{args.url}"
  source_url_checked: {date.today().isoformat()}
  channel: "{info.get('uploader', args.channel)}"
  uploaded: {upload_date}
  duration_min: {duration_min:.0f}
  chapters: {str(bool(chapters)).lower()}

transcript:
  asr_model: "whisper"
  asr_model_version: "{args.whisper_model}"
  asr_implementation: "{versions['whisper'][:80]}"
  ytdlp_version: "{versions['yt-dlp'][:40]}"
  ffmpeg_version: "{versions['ffmpeg'][:80]}"
  segments: {segments}
  transcript_sha256: "{transcript_sha}"
  info_sha256: "{info_sha}"
  chapters_sha256: {f'"{chapters_sha}"' if chapters_sha else "null"}

language:
  content_language: {args.content_language}
  transcript_language: {detected_lang}
  note_language: {args.note_language}

manual_review: {str(gate.manual_review).lower()}
manual_review_reasons: {gate.warns}
---

# {info.get('title', slug)}

**Source:** [{info.get('uploader', args.channel)} — {upload_date}]({args.url})
**Raw transcript:** [[transcript]] (in `raw/videos/{args.category}/{slug}/`)

## Key Takeaways

_(3-5 bullet points to be filled in by INGEST step 8)_

## Notes

_(human-curated synthesis, generated during INGEST step 8 per WIKI-SCHEMA workflow)_
"""
    src_page.write_text(fm, encoding="utf-8")
    log(f"[step 7] wrote source page: {src_page}")

    print(f"\nSUCCESS. Next: complete the source page body and run standard INGEST steps 4-9 (entities, concepts, synthesis, index, log, lint).")
    print(f"Source page: {src_page}")
    print(f"Raw artifacts: {work_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
