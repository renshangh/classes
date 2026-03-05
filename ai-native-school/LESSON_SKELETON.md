# Lesson Skeleton Template (Epic C-2)

This document defines the standardized folder structure for all lesson materials.

## 1. Directory Structure
Each lesson follows this consistent path:
`lessons/[XX]-[slug]/` (e.g., `lessons/01-introduction/`)

```
lessons/[XX]-[slug]/
├── README.md        # Main curriculum (Bilingual side-by-side)
├── handout.md       # Student-facing takeaways (Bilingual stacked)
├── exercise.md      # Timed labs and instructions
├── rubrics.md       # Grading criteria for Sarah/Aether reviewer
└── assets/          # Images, screenshots, and diagrams
```

---

## 2. File Standards

### 2.1 README.md (Bilingual Main)
- Follows the [Bilingual Markdown Standard](BILINGUAL_STANDARD.md).
- Side-by-side tables for all core concepts.

### 2.2 Rubrics.md (Automation Data)
Used by the **Homework Reviewer Skill (E-2)**.
Format:
| Criterion | Points | Description |
| :--- | :--- | :--- |
| Code quality | 5 | Uses clean, readable naming. |
| Prompt precision | 10 | Includes persona, context, and constraints. |

---

## 3. Metadata Schema
Every lesson's `README.md` must include:
```yaml
---
topic: "Lesson Topic"
version: "v1.0"
milestone: "v1.0-alpha"
status: "draft|reviewed|final"
---
```
