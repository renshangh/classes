# Student Progress Tracker

## Overview
This document defines the structure for tracking each student's progress through the AI‑Native School lessons. It is stored in the repository so it can be version‑controlled and referenced by automation scripts.

## Fields
| Field | Type | Description |
|-------|------|-------------|
| `student_id` | string | Unique identifier for the student (e.g., Telegram username or email). |
| `lesson` | string | Lesson identifier (e.g., `lesson-01`, `lesson-02`). |
| `status` | string | Current status of the lesson for the student (see status‑label schema). |
| `last_updated` | ISO datetime | Timestamp of the most recent update. |
| `notes` | string (optional) | Free‑form notes from the instructor or AI assistant. |

## How to Use
- Add a row for each student when they start a lesson.
- Update the `status` field as they progress.
- The `scripts/check_preclass.sh` can be extended to also verify that every student has a tracker entry before a class begins.

## Example (YAML)
```yaml
- student_id: "@alice"
  lesson: "lesson-01"
  status: "in_progress"
  last_updated: "2026-03-08T14:45:00Z"
  notes: "Completed checkpoint 1, needs help with prompt tuning."
```
