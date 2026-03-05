# Proposal: Bilingual Markdown Standard (Epic C-1)

This document defines the side-by-side English/Chinese markdown schema for the AI-Native School curriculum. 

## 1. Goal
To ensure all teaching materials, handouts, and slides are consistently accessible in both English and Chinese, optimized for display on both Desktop (GitHub) and Mobile (Telegram).

---

## 2. Format: Parallel Columns (Markdown Tables)

To achieve a true "side-by-side" look on GitHub, we will use a two-column table as the primary structure for key content blocks.

### 2.1 The Standard Content Block
Every lesson concept or instruction should follow this pattern:

| 🇺🇸 English | 🇨🇳 中文 |
| :--- | :--- |
| **Concept: Prompt Engineering** | **概念：提示词工程** |
| Prompt engineering is the art of crafting precise instructions for AI models to get the best results. | 提示词工程是为 AI 模型编写精确指令，以获得最佳结果的艺术。 |
| *Key Tip: Be specific.* | *关键技巧：描述要具体。* |

### 2.2 Code Blocks & Technical Terms
Technical code blocks remain universal (not translated), but the explanations preceding or following them follow the bilingual table.

---

## 3. Format: Mobile-Optimized (Telegram)

Since **Telegram** is our primary student UI, we must account for its narrow screen. 

### 3.1 The "Stacked" Fallback
While tables work on GitHub, they can be hard to read on phone screens. For Telegram delivery, Sarah/Aether will "stack" the content:

> **🇺🇸 English:** Prompt engineering is the art...
> **🇨🇳 中文:** 提示词工程是为 AI 模型编写...

### 3.2 Emoji Indicators
We will use 🇺🇸 and 🇨🇳 consistently to allow students to visually "scan" for their preferred language.

---

## 4. Folder Structure (Lesson Skeleton)
To keep content organized (Epic C-2), each lesson follows this path:
`lessons/01-lesson-name/`
- `README.md` (The bilingual main content)
- `handout.md` (Student-facing takeaways)
- `assets/` (Images/Slides)

---

## 5. Metadata Header
Every curriculum file must start with:
```yaml
---
topic: "Lesson Name"
version: "v1.0"
milestone: "v1.0-alpha"
language: "Bilingual (EN/ZH)"
---
```
