# Lesson Generator Skill (Epic E-3) Implementation Plan

## 1. Goal
Implement the `lesson-gen` skill to automate the creation of bilingual (EN/ZH) lesson packs following the [Bilingual Standard](BILINGUAL_STANDARD.md) and [Lesson Skeleton](LESSON_SKELETON.md).

## 2. Technical Design
- **Skill Name**: `lesson-gen`
- **Input**: High-level topic string or an outline file.
- **Workflow**:
  1. Create the directory: `ai-native-school/lessons/XX-topic-slug/`.
  2. Generate `README.md` (Main Curriculum) using Side-by-Side tables.
  3. Generate `handout.md` (Student Summary) using Stacked bilingual format.
  4. Generate `exercise.md` and `rubrics.md` based on topic requirements.

## 3. Tool Implementation (Pseudocode/Logic)
```bash
# Example usage
openclaw skill lesson-gen --topic "Introduction to Vectors" --milestone "v1.1-beta"
```

## 4. Prompt Engineering (The "Brain")
The skill will use a specialized system prompt:
> "You are the AI-Native School Content Architect. Your task is to generate lesson materials. 
> ALWAYS use the 🇺🇸/🇨🇳 Side-by-Side table for README.md. 
> ALWAYS use the Stacked emoji-flag format for handout.md.
> Maintain a playful yet intelligent tone (Sarah persona)."

## 5. Next Steps
- Implement the skill logic in a local script.
- Test by generating "Lesson 02: Introduction to Prompting".
- Link to Issue #36.
