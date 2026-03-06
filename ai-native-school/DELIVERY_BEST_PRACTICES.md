# Research: Best Practices for Beginner AI Course Delivery (Issue #3)

This document provides recommendations for delivering the AI-Native School curriculum based on current industry standards and the "Ralph Loop" operational model.

## 1. Delivery Format: Hybrid Model
**Recommendation**: Use a **Live-First, Async-Always** model.

- **Live Sessions**: Focus on "Model Detective" tasks—testing and analyzing chatbot outputs live to build intuition and critical thinking.
- **Async Reinforcement**: Use OpenClaw heartbeats and sub-agents to provide 24/7 support and "nudge" students who stall.

## 2. Materials: Handouts vs. Slides vs. Labs
| Format | Role | Best Practice |
| :--- | :--- | :--- |
| **Handouts** | Reference | Concise, bilingual (EN/ZH), and mobile-optimized for Telegram/Discord. |
| **Slides** | Visual Aid | Minimal text; focus on flowcharts of AI logic and prompt engineering structures. |
| **Labs** | Practical | Scaffolded exercises that start with "Fix this prompt" and move to "Build this agent." |

## 3. Checkpoint Design & Rubrics
- **Low-Stakes Checkpoints**: Quick polls in Telegram/Discord at the end of each session.
- **Rubrics**: Focus on **Process over Result**. Grade students on how they refined their prompts or triaged errors, not just if the final output was "correct."

## 4. Support Model: The "Sarah Triage"
- **Tier 1 (Automated)**: Sarah acknowledges all "I'm Stuck" issues within 5 minutes.
- **Tier 2 (Persona-Led)**: Use sub-agents (Xiao Ming, Evelyn) to provide peer-style hints before escalating to the instructor.
- **Tier 3 (Instructor)**: Randy is tagged only for P0 blockers or complex conceptual questions.

## 5. Implementation Checklist
- [ ] Update `BILINGUAL_STANDARD.md` with mobile-first formatting rules.
- [ ] Create `RUBRIC_TEMPLATE.md` focusing on the "Prompt Refinement" process.
- [ ] Configure Sarah to trigger "Xiao Ming" peer-support hints for common Lesson 01 errors.

## References
- *Sidecar AI*: The Impact of AI-Native Education Platforms.
- *Class Central*: Best Beginner AI Courses for Educators (2026).
- *SchoolAI*: Structured vs. Generic AI in K-12 Education.
