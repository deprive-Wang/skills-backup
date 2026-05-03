param(
    [string]$TargetSkillsRoot = "C:\Users\14000\.codex\skills"
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$CustomDir = Join-Path $RepoRoot "skills\custom"
$CoreDir = Join-Path $RepoRoot "skills\core"
$CommonDir = Join-Path $RepoRoot "skills\common"
$InstallCommands = Join-Path $RepoRoot "catalog\install-commands.md"

function Ensure-Dir([string]$path) {
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path | Out-Null
    }
}

function Restore-SkillDirectory([string]$sourceDir, [string]$targetRoot) {
    if (-not (Test-Path $sourceDir)) {
        return
    }

    Get-ChildItem $sourceDir -Directory | ForEach-Object {
        $destination = Join-Path $targetRoot $_.Name
        if (Test-Path $destination) {
            Remove-Item -LiteralPath $destination -Recurse -Force
        }
        Copy-Item -LiteralPath $_.FullName -Destination $targetRoot -Recurse
        Write-Output "Restored skill: $($_.Name)"
    }
}

Ensure-Dir $TargetSkillsRoot

Restore-SkillDirectory -sourceDir $CustomDir -targetRoot $TargetSkillsRoot
Restore-SkillDirectory -sourceDir $CoreDir -targetRoot $TargetSkillsRoot
Restore-SkillDirectory -sourceDir $CommonDir -targetRoot $TargetSkillsRoot

Write-Output ""
Write-Output "Backup restore completed."
Write-Output "For catalog-only skills, check:"
Write-Output $InstallCommands
