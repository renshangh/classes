# Heartbeat Monitoring – Classroom Material

## What is a Heartbeat?
A *heartbeat* is a lightweight, periodic task that the OpenClaw agent runs to check on external state (e.g., GitHub PR status, CI pipelines, external APIs). It is defined in `HEARTBEAT.md` and can run at any user‑specified interval.

## Our Project’s Heartbeat
- **File:** `HEARTBEAT.md`
- **Location:** `/Users/danielshan/.openclaw/workspace-sarah/HEARTBEAT.md`
- **Schedule:** every **5 minutes**
- **Command:**
  ```bash
  gh pr view 7 --repo renshangh/classes \
      --json number,title,state,reviewDecision,merged,mergeable,comments
  ```
- **Purpose:**
  - Track the status of PR #7 (open/closed/merged)
  - Detect review decisions (`APPROVED`, `CHANGES_REQUESTED`)
  - Pull the latest comments so the agent can react to directives.

## Sample JSON Output
```json
{
  "number": 7,
  "title": "Add placeholder for student‑facing delivery architecture",
  "state": "OPEN",
  "reviewDecision": "APPROVED",
  "merged": false,
  "mergeable": "MERGEABLE",
  "comments": [
    {"body": "Please split the intro into EN/ZH sections."},
    {"body": "#action: merge"}
  ]
}
```

## How We Use the Data
1. **State Changes** – When `state` flips to `MERGED`, the agent posts a concise “PR merged” notice.
2. **Review Decisions** – An `APPROVED` flag can trigger the next step in our Ralph Loop (e.g., start the next issue).
3. **Comments as Triggers** – By agreeing on a simple syntax (e.g., `#action: merge`), anyone can instruct the agent to perform actions directly from the PR discussion.

## Adding New Heartbeat Tasks
1. Open `HEARTBEAT.md`.
2. Add a new line with the desired interval and command, e.g.:
   ```markdown
   - every 10m: gh run list --repo renshangh/classes --limit 1 --json status,name
   ```
3. Save the file – the agent will automatically pick up the new schedule.

---
*This file is part of the OpenClaw beginner class curriculum and demonstrates how automated monitoring can be integrated into a development workflow.*
