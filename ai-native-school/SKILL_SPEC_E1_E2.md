# AI Skill Matrix & HW Reviewer Spec (Epic E-1/E-2)

This document audits current school capabilities and defines the implementation for the automated Homework Reviewer.

## 1. Skill Matrix Audit (Current vs. Needed)

| Skill | Current Source | Capability | Gap for School |
| :--- | :--- | :--- | :--- |
| **github** | OpenClaw | PR/Issue mgmt | Needs "Reviewer" context for rubric mapping. |
| **summarize** | OpenClaw | Text distillation | None. Great for session wrap-ups. |
| **gemini** | OpenClaw | GenAI tasks | Needs prompt tuning for educational rubrics. |
| **HW Reviewer** | *NEW* | Rubric-based grading | **To Be Built**. Must bridge GH PRs to Rubrics. |
| **Lesson Gen** | *NEW* | Bilingual content creation | **To Be Built**. Must enforce Side-by-Side standard. |

---

## 2. Homework Reviewer Spec (E-2)

### 2.1 Trigger
A student submits an issue with the label `homework` and a repository/PR link.

### 2.2 Execution Logic
1. **Fetch**: Aether/Sarah fetches the code/content from the provided link.
2. **Context**: Sarah loads the `rubrics.md` file from the corresponding lesson folder.
3. **Evaluation**: Sarah passes the student code + rubric to an LLM (Gemini/GPT) using a specific "Pedagogical Grader" persona.
4. **Drafting**: A feedback block is generated following the [Assignment & Rubric Template](ASSIGNMENT_RUBRIC_TEMPLATE.md).

### 2.3 Output
Sarah posts the review as a comment on the GitHub issue and pushes a notification to the student's Telegram.

---

## 3. Lesson Generator Spec (E-3)

### 3.1 Trigger
Instructor provides a high-level topic (e.g., "Intro to Vectors").

### 3.2 Execution Logic
1. **Skeleton**: Create folder following [Lesson Skeleton](LESSON_SKELETON.md).
2. **Bilingual Gen**: Generate Side-by-Side tables for all concepts.
3. **Asset Generation**: Suggest diagrams/images needed for the assets folder.
EOF
