# AI Change‑Watch Process (Epic E‑5)

## Purpose
Maintain a monthly review of emerging AI models, tools, and workflows so the OpenClaw school curriculum stays current.

## Steps (repeat each month)
1. **Gather Sources**
   - Official model provider release notes (OpenAI, Anthropic, Google, etc.)
   - Community blogs, research papers (ArXiv, HuggingFace blogs)
   - Tools updates (gog, summarize, etc.)
2. **Run Automated Checks**
   - Use the `gog` CLI to list new releases for services you depend on.
   - Run `summarize` on relevant blog URLs for a quick TL;DR.
3. **Update Documentation**
   - Add a new entry to `ai-native-school/updates/YYYY-MM.md` with a summary.
   - Flag any curriculum sections that need revision.
4. **Notify Stakeholders**
   - Post a summary to the Randy Live Control Board (project #2) as a new item.
   - Send a Telegram reminder to the teaching staff via `@Sarah_closedclawbot`.
5. **Archive**
   - Commit the `updates` markdown file to the repo.
   - Tag the commit with `changewatch-YYYYMM`.

## Template for Monthly Update
```
# YYYY‑MM Update

- **Model releases**: ...
- **Tool updates**: ...
- **Curriculum impact**: ...
- **Action items**: ...
```

## Ownership
- Primary owner: **@Aether**
- Reviewers: **@Sarah**, **@Randy**

---
*This document is part of the AI‑Native School project and should be kept in sync with the project board.*
