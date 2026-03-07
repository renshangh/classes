---
name: class-insights-summarizer
description: Aggregates student checkpoint data, poll results, and common blockers from AI class repositories to provide teaching insights. Use when the user asks for a summary of student progress, common issues in a class session, or a report on class checkpoints.
---

# Class Insights Summarizer

This skill provides a robust, CLI-enabled tool to aggregate student data and evaluate class progress.

## CLI Usage

The core summarizer is a standalone Python CLI. You can run it directly from the command line:

```bash
# General usage
python3 scripts/summarize_class.py <repo_path> <class_id>

# Example
python3 scripts/summarize_class.py . class-1
```

## Quality Assurance & Testing

All code within this skill is verified through automated tests. To run the test suite:

```bash
python3 scripts/test_summarize_class.py
```

## Workflow for AI Agents

1.  **Identify Class Data**: Determine the class ID (e.g., `class-1`).
2.  **Run Summarization Script**: Use the CLI to pull data from the repository.
3.  **Generate Report**: Present the aggregated checkpoints and blockers to the user.
