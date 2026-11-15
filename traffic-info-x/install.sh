#!/usr/bin/env bash
# install.sh — Automated installer for traffic-info-x skill
# Usage:
#   ./install.sh
#   ./install.sh /path/to/skills/dir
#   curl -fsSL https://raw.githubusercontent.com/<owner>/traffic-info-x/main/install.sh | bash

set -euo pipefail

SKILL_NAME="traffic-info-x"
DEFAULT_DIRS=(
  "$HOME/.grok/skills"
  "$HOME/.claude/skills"
  "./skills"
)

TARGET_DIR="${1:-}"

echo "=== Traffic Info X Skill Installer ==="

# Detect target directory
if [[ -z "$TARGET_DIR" ]]; then
  for dir in "${DEFAULT_DIRS[@]}"; do
    if [[ -d "$dir" ]]; then
      TARGET_DIR="$dir"
      break
    fi
  done
fi

if [[ -z "$TARGET_DIR" ]]; then
  TARGET_DIR="$HOME/.grok/skills"
  mkdir -p "$TARGET_DIR"
  echo "Created default skills directory: $TARGET_DIR"
fi

DEST="$TARGET_DIR/$SKILL_NAME"

# If running from within the repo, copy local files
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$SCRIPT_DIR/SKILL.md" ]]; then
  echo "Installing from local directory..."
  rm -rf "$DEST"
  cp -r "$SCRIPT_DIR" "$DEST"
  # Clean unnecessary files if any
  rm -f "$DEST/install.sh"
else
  echo "Local SKILL.md not found. Please run from the skill directory or clone the repo first."
  exit 1
fi

echo ""
echo "✅ Installed to: $DEST"
echo ""
echo "Next steps:"
echo "  1. Restart or reload your agent"
echo "  2. Trigger with: 교통정보 / 교통정보 요약 / 교통정보 안내"
echo ""
echo "Verify:"
echo "  python3 $DEST/validate.py"
