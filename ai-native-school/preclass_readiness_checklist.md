# Pre‑Class Readiness Checklist (Epic B‑1)

## Purpose
Ensure every class starts with the technical, account, and LLM setup fully prepared, in both English and Chinese.

## Checklist (✓ = completed)

| Item | Description | English ✅ | 中文 ✅ |
|------|-------------|-----------|-------|
| **Technical** | Verify required tools and environment are installed. | | |
| • OpenClaw installed (v2.0+) | `openclaw --version` returns a version ≥ 2.0 | | |
| • Python 3.11+ installed | `python3 --version` shows 3.11 or higher | | |
| • Required CLI tools (`gog`, `summarize`, `codexbar`) are accessible | `which gog && which summarize && which codexbar` | | |
| **Account** | Confirm all necessary accounts are active and linked. | | |
| • Google Workspace (Gmail/Calendar/Drive) linked | Token stored in `~/.gog/config.json` | | |
| • OpenAI/Claude API keys configured | `echo $OPENAI_API_KEY && echo $ANTHROPIC_API_KEY` | | |
| • Telegram bot token set (for @Sarah_closedclawbot) | `echo $TELEGRAM_BOT_TOKEN` | | |
| **LLM Readiness** | Prepare the model environment for the lesson. | | |
| • Model version matches lesson requirements (e.g., Gemini 1.5 Flash) | `openclaw status` shows correct model | | |
| • Prompt templates for the lesson are in `ai-native-school/prompts/lesson-01/` | Files exist and are up‑to‑date | | |
| **Materials** | Verify lesson assets are available. | | |
| • Handout and support guide uploaded to Google Drive (share link in repo) | Links in `ai-native-school/lessons/01-intro/` README | | |
| • Bilingual markdown files (`*.en.md` and `*.zh.md`) present for all lesson sections | `ls ai-native-school/lessons/01-intro/*` | | |

## Usage
- Before each class, the instructor runs `./scripts/check_preclass.sh` which reads this file and prints any unchecked items.
- The script exits with a non‑zero status if any ✅ box is empty, preventing the class from starting.

## Example script (bash)
```bash
#!/usr/bin/env bash
set -e

grep -v "| ✓" ai-native-school/preclass_readiness_checklist.md || {
  echo "❌ Some pre‑class items are missing! Fix them before the session."
  exit 1
}

echo "✅ All pre‑class checks passed. Ready to start!"
```

---
*Keep this checklist version‑controlled; update it whenever new tools or requirements are added.*
