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
7. **Post concise status**:
   - what changed
   - evidence (tests/checks)
   - blocker or next action
8. **Persist state** in files (`TASK.md`, optional `STATUS.md`) so restart can resume
9. Repeat next cycle

### C. Stop Conditions
- No actionable issue remains
- Blocked by missing decision/credentials/approval
- Failing checks with no safe auto-fix path

### D. Restart Recovery Rules
After gateway/agent restart:
1. Read `TASK.md` first
2. Resume item marked `IN_PROGRESS`
3. If none marked, resume highest-priority `TODO`
4. Re-validate branch/PR state before new work

### E. Privacy Guardrails
- Never post personal health/schedule/project-private details to group chats.
- Group updates must be sanitized, task-focused, and minimal.
- Sensitive context stays in private session/files only.

---

## 3) Working Queue

### IN_PROGRESS
- [ ] Implement Issue #5: Student‑Facing Delivery Architecture (EN/ZH)

### NEXT
- [ ] Confirm pending PR is approved by Randy
- [ ] Pull latest default branch after approval
- [ ] Identify next open issue to implement
- [ ] Start first Ralph cycle on that issue

### BACKLOG
- [ ] Add `STATUS.md` template for per-cycle logs
- [ ] Add restart checklist script/doc (quick recovery steps)
- [ ] Add "group-safe summary" template for public updates
- [ ] **Issue #9** – Set up Google Drive folder for classroom infrastructure

### BLOCKED / NEEDS HUMAN INPUT
- [ ] Repository + issue source to target next (repo name / issue list)
- [ ] Merge policy preference (squash/rebase/merge)
- [ ] Required CI gates before PR is considered ready

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
  - Example: "Issue X implemented, PR #123 ready for review, CI passing."

---

## 6) Immediate Next Action
Once Randy approves pending PR, begin the first post-approval cycle:
1. Sync branch
2. Pick next issue
3. Implement and open/update PR
4. Report status
