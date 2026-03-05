# Proposal: Telegram Student UI & Interaction Model (Epic B-1)

This document defines how students will interact with the "AI-Native School" primarily through Telegram.

## 1. Core Principles
- **Low Friction**: Everything should be accessible without leaving Telegram.
- **Push-First**: Materials and reminders are pushed to the student.
- **Asynchronous Help**: Students use the bot to trigger "stuck-protocol" support.

---

## 2. Interaction Flows

### 2.1 Pre-Class Readiness (B-1)
- **Checklist Push**: 24h before class, the bot sends a bilingual checklist.
- **Status Check**: Students tap an inline button "✅ Ready" or "❓ Help needed".
- **Bot Response**: If "Help needed", the bot asks for a screenshot and opens a GitHub issue tagged `student-help`.

### 2.2 In-Class Materials (C-2 Integration)
- **Delivery**: Bot sends the "Stacked" bilingual content blocks (from Epic C-1 standard).
- **Checkpoints**: After each concept, the bot sends a poll: "Did you catch that?"
  - 👍 (Understood)
  - 🤔 (Need more detail)
  - 🛑 (Stuck)

### 2.3 Homework Submission (E-2 Integration)
- **Flow**: Student sends `/submit [Repo URL]`.
- **Sarah/Aether Response**: "Received! Sarah is reviewing your homework against the rubric now..."
- **Feedback Loop**: Once the Homework Reviewer skill finishes, the bot pushes the feedback directly to the chat.

---

## 3. UI Components (Bot Controls)
- **Main Menu**: Persistent buttons for `[📚 Current Lesson]`, `[📝 Homework Status]`, `[🚨 I'm Stuck]`.
- **Inline Buttons**: Used for quick confirmations and poll responses.

---

## 4. Support Triage (A-4)
- When a student is stuck, they trigger a "Triage" flow.
- The bot asks for:
  1. Description of the error.
  2. Screenshot (if applicable).
- A GitHub issue is created, and the Instructor (Randy) is notified via a priority alert.
