#!/usr/bin/env bash
set -e

# Path to the checklist file (relative to repository root)
CHECKLIST="ai-native-school/preclass_readiness_checklist.md"

# Find any unchecked rows (those without a tick in both columns)
if grep -v "| ✓" "$CHECKLIST" | grep "|   |"; then
  echo "❌ Some pre‑class items are missing! Fix them before the session."
  exit 1
else
  echo "✅ All pre‑class checks passed. Ready to start!"
fi
