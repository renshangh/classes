# QA Strategy & Pilot Test Cases (Issue #46)

This document outlines the testing framework for the AI-Native School, ensuring bot-student interactions are high-quality and triage protocols are robust.

## 1. Testing Objectives
- Validate content accessibility (Bilingual EN/ZH).
- Test response latency and accuracy of the Sarah bot.
- Verify the "I'm Stuck" triage flow triggers appropriate owner notifications.

## 2. Student Personas (Sub-Agent Simulation)
To test the curriculum, Sarah spawns sub-agents with specific profiles:

| Name | Level | Profile | Focus |
| :--- | :--- | :--- | :--- |
| **Xiao Ming** | Beginner | Non-technical, asks for clarification often. | UX, Clarity, Handouts. |
| **Evelyn** | Intermediate | Some coding knowledge, tests edge cases. | Logic, Exercises. |
| **Ken** | Advanced | Professional, focuses on integration. | Depth, Real-world use. |

## 3. Test Cases (Lesson 01 Pilot)
| ID | Title | Description | Expected Outcome |
| :--- | :--- | :--- | :--- |
| **TC-01** | Initial Greeting | Student enters chat. | Sarah greets with bilingual intro and links to handout. |
| **TC-02** | Stalled Progress | Student doesn't reply for 2h. | Heartbeat triggers a gentle nudge. |
| **TC-03** | Blocker Triage | Student logs "I'm Stuck" issue. | Sarah acknowledges and tags Randy if P0. |
| **TC-04** | Homework Submission | Student submits via issue. | Sarah triggers Homework Reviewer skill. |

## 4. Success Criteria
- **Clarity**: >90% of sub-agent queries are resolved without manual instructor intervention.
- **Latency**: Sarah acknowledges critical issues in <5 minutes.
- **Bilingualism**: All materials and automated replies include both EN and ZH versions.
