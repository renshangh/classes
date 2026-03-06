# Skills Backlog: Class Operations (Issue #4)

This document maps AI-Native School operations to OpenClaw skills, identifying existing tools to enable and new skills to build.

## 1. Operations vs. Skills Matrix

| Operation | Skill/Tool | Priority | Status |
| :--- | :--- | :--- | :--- |
| **Lesson Generation** | `lesson_gen.py` | P0 | 🛠️ Prototype |
| **Class Insights** | `class_insights.py` | P1 | 🛠️ Prototype |
| **Homework Review** | `homework_reviewer` | P0 | ⏭️ Backlog |
| **Multilingual Sync** | `bilingual_sync` | P1 | ⏭️ Backlog |
| **Issue Triage** | `triage_agent` | P0 | ⏭️ Backlog |
| **Transcript Summary** | `summarize` (core) | P2 | ✅ Enabled |

## 2. Proposed Custom Skill Specs

### A. Homework Reviewer (Epic E-3/E-4)
- **Goal**: Automatically grade student submissions against `rubrics.md`.
- **Logic**: Triggered by `homework` label on GitHub issues. Sarah reads the attached file/text, compares it to the rubric, and posts a comment with feedback.

### B. Bilingual Sync (Epic C-1)
- **Goal**: Ensure EN and ZH versions of all materials remain synchronized.
- **Logic**: Triggered by a PR merge. Scans for missing translations in `.en.md` vs `.zh.md` and generates a "Translation Needed" report.

### C. Triage Agent (Epic I-1)
- **Goal**: Speed up the "I'm Stuck" response time.
- **Logic**: Uses RAG to search `SUPPORT_GUIDE.md` and `QA_STRATEGY.md` to provide immediate peer-style hints (Xiao Ming persona) before Randy is paged.

## 3. Implementation Plan
- [ ] Finalize `homework_reviewer` spec and implementation path (Issue #36/37).
- [ ] Integrate `triage_agent` logic into the primary Sarah loop.
- [ ] Enable `summarize` skill for post-class transcript processing.
