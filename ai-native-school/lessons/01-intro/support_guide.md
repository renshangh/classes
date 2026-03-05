# Support Triage Protocol (Epic A-4)

This document defines the automated support triage flow for students.

## 1. Triggering Triage
Students can trigger the triage flow in Telegram using:
- The **"🚨 I'm Stuck"** persistent menu button.
- The **"🛑 (Stuck)"** inline button on lesson checkpoints.

## 2. Information Collection (Bot Flow)
When triggered, the Sarah/Aether bot follows this sequence:
1. **Query**: "I'm sorry you're stuck! Please describe what's happening."
2. **Screenshot**: "If there's an error message, please send a screenshot now."
3. **Confirmation**: "Got it. I'm opening a support ticket for you now. Stay tuned!"

## 3. GitHub Automation
The bot automatically creates a GitHub issue with:
- **Title**: `[Support] Student Stuck: [Summary]`
- **Labels**: `student-help`, `triage`, `epic-A`
- **Body**: Includes the student's description, session context, and a link to the uploaded screenshot.

## 4. Response SLA
- **Immediate**: Bot acknowledges the issue and provides the GitHub issue link.
- **Priority 1 (SLA < 5 min during class)**: Instructor (Randy) receives a high-priority alert.
- **Resolution**: Once resolved, the GitHub issue is closed, and the bot pushes a "✅ Resolved" notification to the student.
