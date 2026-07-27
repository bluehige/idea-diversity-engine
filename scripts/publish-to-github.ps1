param(
  [string]$Repo = "bluehige/idea-diversity-engine"
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  throw "Git is required."
}
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
  throw "GitHub CLI (gh) is required for automatic repository creation."
}

gh auth status
if (-not (Test-Path .git)) {
  git init -b main
  git add .
  git commit -m "chore: public release v0.1.0"
}

gh repo create $Repo --public --source . --remote origin --push 
Write-Host "Published: https://github.com/$Repo"
