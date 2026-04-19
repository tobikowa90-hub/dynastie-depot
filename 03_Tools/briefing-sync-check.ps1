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
$briefingFiles = @(
    '00_Core/STATE.md',
    '00_Core/Faktortabelle.md',
    '00_Core/CORE-MEMORY.md',
    '00_Core/SESSION-HANDOVER.md',
    '00_Core/INSTRUKTIONEN.md'
)

# Check 1: uncommitted changes in briefing files
$dirtyCount = 0
try {
    $statusOutput = & git status --porcelain @briefingFiles 2>$null
    if ($statusOutput) {
        $dirtyCount = ($statusOutput | Where-Object { $_ -and $_.Trim() }).Count
    }
} catch {}

# Check 2: commits ahead of origin/main touching 00_Core/
$unpushedCount = 0
try {
    $revOutput = & git rev-list --count 'origin/main..HEAD' -- '00_Core/' 2>$null
    if ($revOutput -match '^\d+$') {
        $unpushedCount = [int]$revOutput
    }
} catch {}

# Threshold: only warn when noise becomes actionable
# Uncommitted changes are always relevant (user has unsaved work).
# Unpushed commits only matter in bulk — <3 is just normal session churn.
$unpushedThreshold = 5

if ($dirtyCount -eq 0 -and $unpushedCount -lt $unpushedThreshold) {
    Write-Output '{}'
    exit 0
}

# Dirty state → build message
$parts = @()
if ($dirtyCount -gt 0)   { $parts += "$dirtyCount uncommitted" }
if ($unpushedCount -gt 0) { $parts += "$unpushedCount unpushed" }
$detail = $parts -join ', '
$msg = "BRIEFING-SYNC ausstehend: $detail in 00_Core/. Das Morning-Briefing 10:00 liest sonst veraltete Daten aus GitHub. Fuehre !SyncBriefing aus."

# Fire Windows Toast (native WinRT, no dependencies)
try {
    [void][Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]
    [void][Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime]

    $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent(
        [Windows.UI.Notifications.ToastTemplateType]::ToastText02
    )
    $textNodes = $template.GetElementsByTagName('text')
    [void]$textNodes.Item(0).AppendChild($template.CreateTextNode('Dynasty-Depot: Briefing-Sync ausstehend'))
    [void]$textNodes.Item(1).AppendChild($template.CreateTextNode("$detail in 00_Core/ - !SyncBriefing vor naechster Session"))

    $toast = [Windows.UI.Notifications.ToastNotification]::new($template)
    [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('DynastyDepot').Show($toast)
} catch {
    # Toast failed (non-Windows, missing WinRT, etc.) — terminal warning still fires via JSON
}

# Emit JSON systemMessage to stdout for Claude Code hook consumption
$payload = @{ systemMessage = $msg } | ConvertTo-Json -Compress
Write-Output $payload
exit 0
