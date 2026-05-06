param(
    [string]$SourceWorkflowsRoot = "C:\Users\14000\Documents\Codex\2026-05-02\planing-with-file-skill",
    [string]$SourceSkillsRoot = "C:\Users\14000\.codex\skills"
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$CoreWorkflowDir = Join-Path $RepoRoot "core-workflows"
$CustomDir = Join-Path $RepoRoot "skills\custom"
$CoreDir = Join-Path $RepoRoot "skills\core"
$CommonDir = Join-Path $RepoRoot "skills\common"

$workflowFiles = @(
    "thesis-workflow.md",
    "coding-workflow.md",
    "daily-skill-combos.md"
)

$customSkills = @(
    "planing-with-file",
    "code-simplifier",
    "codex-project-onboarding"
)

$coreSkills = @(
    "create-plan",
    "content-research-writer",
    "paperjsx",
    "spreadsheet-formula-helper",
    "meeting-notes-and-actions",
    "meeting-insights-analyzer",
    "tdd",
    "diagnose",
    "webapp-testing",
    "zoom-out",
    "file-organizer",
    "neat-freak"
)

$commonSkills = @(
    "edit-article",
    "hv-analysis",
    "grill-me",
    "grill-with-docs",
    "notion-research-documentation",
    "notion-spec-to-implementation",
    "obsidian-vault",
    "pdf",
    "doc"
)

function Ensure-Dir([string]$path) {
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path | Out-Null
    }
}

function Sync-File([string]$source, [string]$destinationDir) {
    Ensure-Dir $destinationDir
    if (-not (Test-Path $source)) {
        throw "Missing workflow file: $source"
    }
    Copy-Item -LiteralPath $source -Destination $destinationDir -Force
}

function Sync-Skill([string]$sourceRoot, [string]$skillName, [string]$destinationRoot) {
    $source = Join-Path $sourceRoot $skillName
    $destination = Join-Path $destinationRoot $skillName

    if (-not (Test-Path $source)) {
        throw "Missing skill source: $source"
    }

    if (Test-Path $destination) {
        Remove-Item -LiteralPath $destination -Recurse -Force
    }

    Ensure-Dir $destinationRoot
    Copy-Item -LiteralPath $source -Destination $destinationRoot -Recurse
}

foreach ($wf in $workflowFiles) {
    Sync-File -source (Join-Path $SourceWorkflowsRoot $wf) -destinationDir $CoreWorkflowDir
}

foreach ($skill in $customSkills) {
    Sync-Skill -sourceRoot $SourceSkillsRoot -skillName $skill -destinationRoot $CustomDir
}

foreach ($skill in $coreSkills) {
    Sync-Skill -sourceRoot $SourceSkillsRoot -skillName $skill -destinationRoot $CoreDir
}

foreach ($skill in $commonSkills) {
    Sync-Skill -sourceRoot $SourceSkillsRoot -skillName $skill -destinationRoot $CommonDir
}

Push-Location $RepoRoot
try {
    git add .
    $status = git status --porcelain
    if (-not $status) {
        Write-Output "nothing to sync"
        exit 0
    }

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    git commit -m "sync codex skills backup $timestamp"

    $hasRemote = git remote
    if ($hasRemote) {
        git push
    } else {
        Write-Output "Committed locally. No remote configured yet."
    }
}
finally {
    Pop-Location
}
