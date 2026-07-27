#!/usr/bin/env bash
set -euo pipefail
REPO="${1:-bluehige/idea-diversity-engine}"
command -v git >/dev/null
command -v gh >/dev/null
gh auth status
if [ ! -d .git ]; then
  git init -b main
  git add .
  git commit -m "chore: public release v0.1.0"
fi
gh repo create "$REPO" --public --source . --remote origin --push
echo "Published: https://github.com/$REPO"
