#Requires -Version 5.1

# briefing-sync-check.ps1 — STATE/CORE-MEMORY/Faktortabelle → Remote-Trigger-Sync
# Kontext (19.04.2026): Unterstützt §18 Sync-Pflicht und §29.5 Sin #2 Look-Ahead-Prevention
# (Point-in-Time-Persistenz kritisch für spätere Retrospective-Validation).

<#
.SYNOPSIS
  Dynasty-Depot Briefing-Sync Check
.DESCRIPTION
  Fires on SessionStart and SessionEnd via Claude Code hooks.
  Checks if briefing-relevant files in 00_Core/ are uncommitted or unpushed.
  On dirty state:
    1. Emits JSON systemMessage to stdout (Claude Code CLI shows warning)
    2. Fires native Windows Toast notification (no external modules required)
  On clean state: silent (emits empty JSON).
.NOTES
  Called from .claude/settings.local.json hooks.
  Windows-Toast uses native WinRT API — works on Win10/11 without BurntToast.
#>

$ErrorActionPreference = 'SilentlyContinue'
$projectRoot = 'C:\Users\tobia\OneDrive\Desktop\Claude Stuff'

# Guard: if project root doesn't exist, exit silently
if (-not (Test-Path -LiteralPath $projectRoot)) {
    Write-Output '{}'
    exit 0
}

Set-Location -LiteralPath $projectRoot

# Briefing-relevant files (what morning-briefing trigger reads from repo)
# Includes 01_Skills/dynastie-depot/config.yaml since §18 v2.1 (25.04.2026):
# config.yaml is part of the score-event-set, drift desyncs satellite-state vs PORTFOLIO/Faktortabelle.
$briefingFiles = @(
    '00_Core/STATE.md',
    '00_Core/PORTFOLIO.md',
    '00_Core/PIPELINE.md',
    '00_Core/SYSTEM.md',
    '00_Core/Faktortabelle.md',
    '00_Core/CORE-MEMORY.md',
    '00_Core/SESSION-HANDOVER.md',
    '00_Core/INSTRUKTIONEN.md',
    '01_Skills/dynastie-depot/config.yaml'
)

# Check 1: uncommitted changes in briefing files
$dirtyCount = 0
try {
    $statusOutput = & git status --porcelain @briefingFiles 2>$null
    if ($statusOutput) {
        $dirtyCount = ($statusOutput | Where-Object { $_ -and $_.Trim() }).Count
    }
} catch {}

# Check 2: commits ahead of origin/main touching 00_Core/ or dynastie-depot config.yaml
$unpushedCount = 0
try {
    $revOutput = & git rev-list --count 'origin/main..HEAD' -- '00_Core/' '01_Skills/dynastie-depot/config.yaml' 2>$null
    if ($revOutput -match '^\d+$') {
        $unpushedCount = [int]$revOutput
    }
} catch {}

# Threshold: only warn when noise becomes actionable
# Uncommitted changes are always relevant (user has unsaved work).
# Unpushed commits only matter in bulk — <5 is just normal session churn.
$unpushedThreshold = 5

# Earnings-Calendar Drift-Check (additive, fail-soft)
# Ruft earnings_calendar.py --json auf, parst Drift-Liste; 11 Tickers x ~500B JSON ~5KB total.
$earningsBlock = $null
$earningsDriftMsg = ""
try {
    $earningsRaw = & python "$projectRoot\03_Tools\earnings_calendar.py" --check --json 2>$null
    if ($LASTEXITCODE -in 0,2 -and $earningsRaw) {
        $earningsBlock = ($earningsRaw -join "`n") | ConvertFrom-Json
    }
} catch {
    # Silent - Tool-Crash darf den Owner-Hook nicht brechen.
    $earningsBlock = $null
}

if ($earningsBlock -and $earningsBlock.summary.drifts -gt 0) {
    $driftItems = $earningsBlock.items | Where-Object { $_.drift_status -eq "DRIFT" }
    $driftLines = $driftItems | ForEach-Object {
        "  - $($_.ticker) $($_.earnings_date) ($($_.days_until)d, $($_.source))"
    }
    $earningsDriftMsg = "Earnings-Calendar Drift ($($earningsBlock.summary.drifts)):`n" + ($driftLines -join "`n")
}

if ($dirtyCount -eq 0 -and $unpushedCount -lt $unpushedThreshold -and -not $earningsDriftMsg) {
    Write-Output '{}'
    exit 0
}

# Dirty state -> build combined message
$parts = @()
if ($dirtyCount -gt 0)   { $parts += "$dirtyCount uncommitted" }
if ($unpushedCount -gt 0) { $parts += "$unpushedCount unpushed" }

$msgSegments = @()
if ($parts.Count -gt 0) {
    $detail = $parts -join ', '
    $msgSegments += "BRIEFING-SYNC ausstehend: $detail in 00_Core/ + dynastie-depot config.yaml. Das Morning-Briefing 10:00 liest sonst veraltete Daten aus GitHub. Fuehre !SyncBriefing aus."
}
if ($earningsDriftMsg) {
    $msgSegments += $earningsDriftMsg
}
$msg = $msgSegments -join "`n`n"

# Fire Windows Toast (native WinRT, no dependencies) - only when briefing-sync triggers
if ($parts.Count -gt 0) {
    try {
        [void][Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]
        [void][Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime]

        $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent(
            [Windows.UI.Notifications.ToastTemplateType]::ToastText02
        )
        $textNodes = $template.GetElementsByTagName('text')
        [void]$textNodes.Item(0).AppendChild($template.CreateTextNode('Dynasty-Depot: Briefing-Sync ausstehend'))
        [void]$textNodes.Item(1).AppendChild($template.CreateTextNode("$detail in 00_Core/+config.yaml - !SyncBriefing vor naechster Session"))

        $toast = [Windows.UI.Notifications.ToastNotification]::new($template)
        [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('DynastyDepot').Show($toast)
    } catch {
        # Toast failed (non-Windows, missing WinRT, etc.) - terminal warning still fires via JSON
    }
}

# Emit JSON systemMessage to stdout for Claude Code hook consumption
$payload = @{ systemMessage = $msg } | ConvertTo-Json -Compress
Write-Output $payload
exit 0
