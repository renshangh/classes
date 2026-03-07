# Lesson Pack Generator Skill (Epic E-3)

## Goal
Automate the creation of bilingual (EN/ZH) lesson materials, including handouts, exercises, and rubrics, from a high-level topic or outline.

## Inputs
- `--topic`: The main subject of the lesson.
- `--outline` (optional): A markdown list of key points to cover.
- `--milestone` (optional): The target version/milestone for the lesson.

## Logic Flow
1. **Directory Setup**: Create a standardized folder `lessons/[XX]-[slug]/`.
2. **Content Generation**:
   - Use LLM to generate side-by-side bilingual content for `README.md`.
   - Generate student-facing `handout.md` with key takeaways.
   - Generate practical `exercise.md` with clear submission steps.
   - Generate `rubrics.md` for automated grading.
3. **Validation**: Ensure all files follow the `BILINGUAL_STANDARD.md`.

## Integration
- Triggered via OpenClaw CLI: `openclaw skill lesson-gen ...`
- Outputs are pushed to a new branch for PR review.
