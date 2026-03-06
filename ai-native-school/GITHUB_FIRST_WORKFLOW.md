# GitHub-First Teaching Workflow (Issue #2)

This document establishes the official operating model for the AI‑Native School, ensuring all class delivery, homework, and support are tracked and managed through GitHub.

## 1. Source of Truth: Repository Structure
All teaching materials reside in the `classes` repository under the following structure:
- `lessons/[XX]-[slug]/`: Standardized lesson folders (Epic C‑2).
- `TASK.md`: High‑level control plane for the active sprint.
- `.github/ISSUE_TEMPLATE/`: Structured forms for student and staff input.

## 2. Delivery Flow (Sarah)
- **Sarah (Lead & Sole Role)**:
  - Manages the `TASK.md` and project roadmap.
  - Pushes curriculum content via Pull Requests for review.
  - Monitors the "I'm Stuck" triage flow.
  - Conducts content accuracy audits.
  - Handles automated grading via the "Homework Reviewer" skill.
  - Cross‑posts relevant updates to Telegram.

## 3. Homework Submission & Feedback
1. **Submission**: Students use the `📝 Homework Submission` issue template.
2. **Detection**: Sarah detects new issues with the `homework` label.
3. **Grading**: Sarah triggers the "Homework Reviewer" skill to post feedback against the lesson's `rubrics.md`.
4. **Resolution**: The issue is closed once the student acknowledges the feedback or completes the requested revisions.

## 4. Support & Triage (The "Stuck Protocol")
1. **Report**: Student creates a `🛑 I'm Stuck!` issue.
2. **Triage**: Sarah acknowledges the issue within 5 minutes (during class hours).
3. **Escalation**: If Sarah cannot resolve the blocker, she tags the Instructor (Randy) and escalates the issue status to `priority:P0`.

## 5. Review & Versioning
- All content changes must go through a Pull Request (`develop` → `main`).
- Lessons are versioned using GitHub Milestones (e.g., `v1.0‑alpha`).
- A "Curriculum Freshness Review" is conducted monthly via GitHub Project board automation.

## 6. Project Board Integration
- All tasks must be linked to the [Randy Project Control Board](https://github.com/users/renshangh/projects/2).
- Status changes in GitHub Issues (Inbox, Ready, Doing, Done) should automatically reflect on the Project Board.
- Sarah is responsible for maintaining the "Sarah Ownership" view on the board.
