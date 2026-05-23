import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from backlink import BacklinkHit, BacklinkReport, scan_backlinks  # noqa: E402

FIXTURES = Path(__file__).parent / "fixtures"


def test_backlink_scanner_finds_positive_hits():
    report = scan_backlinks(
        scan_paths=[FIXTURES],
        search_terms=["§13"],
        case_sensitive=True,
    )
    assert isinstance(report, BacklinkReport)
    assert len(report.hits) >= 2
    assert all(isinstance(h, BacklinkHit) for h in report.hits)
    pos_path = (FIXTURES / "backlink_positive.md").resolve()
    assert any(h.file == pos_path for h in report.hits)


def test_backlink_scanner_clean_file_no_hits():
    report = scan_backlinks(
        scan_paths=[FIXTURES / "backlink_clean.md"],
        search_terms=["§13"],
        case_sensitive=True,
    )
    assert len(report.hits) == 0


def test_backlink_scanner_multi_term():
    report = scan_backlinks(
        scan_paths=[FIXTURES / "backlink_positive.md"],
        search_terms=["§13", "§13.X"],
        case_sensitive=True,
    )
    terms_found = {h.term for h in report.hits}
    assert "§13" in terms_found
    assert "§13.X" in terms_found
