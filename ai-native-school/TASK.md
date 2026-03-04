# TASK.md — Closed-claw Project Workflow (Ralph Loop Style)

## 1) Goal
Create a reliable, restart-safe, privacy-safe workflow so Sarah can keep progressing on issues with minimal supervision.

---

## 2) Operating Policy (Workflow First)

### A. Scope Gate (MUST run first each cycle)
1. Detect chat context:
   - **Group chat** → public-safe mode only (no personal memory/details)
   - **Direct/private work session** → full project execution mode
2. Reject/redirect sensitive tasks if context is group and content is private.

### B. Ralph Loop Cycle (one issue per cycle)
1. **Pick next item** from backlog (`TASK.md` queue below)
2. **Create/update branch** for that single item
3. **Implement** smallest shippable change
4. **Run checks** (tests/lint/build as available)
5. **Commit + push** with clear message
6. **Open or update PR**
7. **Post concise status**
8. **Persist state** in files (`TASK.md`, optional `STATUS.md`) so restart can resume
9. Repeat next cycle

---

## 3) Working Queue

### DONE
- [x] **Define and finalize this workflow** with Randy (owner approval)
- [x] **Issue #5** — Implement Student-facing delivery architecture (EN/ZH)

### IN_PROGRESS
- [ ] **Issue #9** — Set up Google Drive folder for classroom infrastructure (Blocked: Needs `gog` auth)

### NEXT
- [ ] **Epic D-4 & D-5** — Setup Label Taxonomy and Milestone Scheme on GitHub
- [ ] **Epic C-1 & C-2** — Define Bilingual Content Standard and Lesson Skeleton

### BACKLOG (ai-native-school Roadmap)

#### Epic A: Teaching Delivery OS
- [ ] **A-1** — Runbook: Live class workflow
- [ ] **A-2** — Runbook: Demo protocol
- [ ] **A-3** — Runbook: Exercise protocol
- [ ] **A-4** — Runbook: In-class issue triage

#### Epic B: Student Experience System
- [ ] **B-1** — Checklist: Pre-class readiness
- [ ] **B-2** — Template: Post-class reinforcement loop
- [ ] **B-3** — Form: Stuck-protocol issue template
- [ ] **B-4** — Tracker: Student progress board

#### Epic C: Content Architecture
- [ ] **C-1** — Standard: Bilingual content format (EN/ZH)
- [ ] **C-2** — Template: Lesson skeleton
- [ ] **C-3** — Template: Assignment & rubric
- [ ] **C-4** — Pattern: Teacher-vs-student handouts

#### Epic D: GitHub Workflow + Automation
- [ ] **D-1** — Issue template: Homework submission
- [ ] **D-2** — Issue template: Blocker / help request
- [ ] **D-3** — PR template: Content update checklist
- [ ] **D-4** — Label taxonomy
- [ ] **D-5** — Milestone scheme

#### Epic E: AI Skills Roadmap (OpenClaw)
- [ ] **E-1** — Skill matrix: Current vs needed
- [ ] **E-2** — Skill: Homework reviewer
- [ ] **E-3** — Skill: Lesson pack generator
- [ ] **E-4** — Skill: Class insights summarizer
- [ ] **E-5** — Skill: EN-ZH pedagogy translator
- [ ] **E-6** — Process: AI change-watch

#### Epic F: Quality & Future-Proofing
- [ ] **F-1** — KPI definition: Learning metrics
- [ ] **F-2** — Review: Curriculum freshness (monthly)
- [ ] **F-3** — Release process: Versioned material packs
- [ ] **F-4** — Pilot: New AI tool integration

#### Project Foundation (Original Issues)
- [ ] **Issue #4** — Decide which OpenClaw skills to enable/build for class operations
- [ ] **Issue #3** — Research best ways to deliver AI course materials to students
- [ ] **Issue #2** — Define GitHub-first teaching workflow

---

## 4) Definition of Done (per issue)
- Code implemented and pushed
- Relevant checks pass (or failures documented with cause)
- PR opened/updated with summary
- `TASK.md` updated (`IN_PROGRESS` -> done, next item promoted)

---

## 5) Communication Pattern
- **Private work thread/session:** full detail
- **Group chat:** short safe status only

---

## 6) Immediate Next Action
1. Resolve `gog` authentication for Issue #9.
2. Begin Epic D-4/D-5 (GitHub Infrastructure).
