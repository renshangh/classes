---
name: class-insights-summarizer
description: Aggregates student checkpoint data, poll results, and common blockers from AI class repositories to provide teaching insights. Use when the user asks for a summary of student progress, common issues in a class session, or a report on class checkpoints.
---

# Class Insights Summarizer

This skill aggregates data from student submissions and checkpoint responses to help teachers identify blockers and assess class progress.

## When to Use

- "How is the class doing on the checkpoints?"
- "Summarize common student blockers for Class 1."
- "What's the success rate for Lesson 01?"

## Workflow

1.  **Identify Class Data**: Determine the class ID (e.g., `class-1`, `class-2`).
2.  **Run Summarization Script**: Use `scripts/summarize_class.py` to pull data from the repository.
3.  **Generate Report**: Present the aggregated checkpoints and blockers to the user.

## Example

```bash
python3 scripts/summarize_class.py . class-1
```
