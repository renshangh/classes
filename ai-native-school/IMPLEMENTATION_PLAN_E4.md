# Class Insights Summarizer Skill (Epic E-4) Implementation Plan

## 1. Goal
Implement the `class-insights` skill to provide the instructor with a summary of student comprehension based on Telegram checkpoint polls and triage data.

## 2. Technical Design
- **Skill Name**: `class-insights`
- **Input**: List of Telegram poll results (JSON) and recent "I'm Stuck" issues from GitHub (filtered by milestone/lesson).
- **Workflow**:
  1. Retrieve poll data for the active lesson session.
  2. Fetch GitHub issues tagged `student-help` and `triage` within the last session's timeframe.
  3. Analyze data to identify "Top 3 Blockers" and "Comprehension Rate."

## 3. Tool Implementation (Logic)
```bash
# Example usage
openclaw skill class-insights --lesson "01-intro"
```

## 4. Output (The "Sarah Report")
Sarah generates a concise instructor update:
> **📊 Class Insights: [Lesson Name]**
> **Comprehension Rate**: 85% understood, 15% need more detail.
> **Current Blockers**: [Common issues].
> **Recommendation**: "Students are struggling with [Specific step]. Suggest a quick live recap or updated handout."

## 5. Next Steps
- Implement logic to poll GitHub issues for specific milestone/timeframe metadata.
- Test by summarizing data from the "Xiao Ming" pilot QA run.
- Link to Issue #37.
