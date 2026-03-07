"""Lesson Generator Skill (E-3) – Prototype

This is a minimal prototype of the `lesson-gen` OpenClaw skill.
It demonstrates the expected interface and workflow without
going into full LLM prompting.

Usage (via OpenClaw CLI):
    openclaw skill lesson-gen --topic "<high‑level topic>" [--milestone <milestone>]

The script will:
1. Create a sanitized slug from the topic.
2. Create the lesson directory under `ai-native-school/lessons/XX‑slug/`.
3. Generate the required files (`README.md`, `handout.md`, `exercise.md`, `rubrics.md`).
4. Populate each file with placeholder content that follows the
   Bilingual Standard and Lesson Skeleton.

The real implementation will replace the placeholders with LLM‑generated
content using the `lesson-gen` skill prompt.
"""
import os, sys, argparse, datetime, re, json

def slugify(text):
    # Simple slug: lower, replace spaces with '-', keep alphanum
    return re.sub(r'[^a-z0-9-]', '', re.sub(r'\s+', '-', text.lower()))

def create_lesson(topic, outline=None, milestone=None):
    slug = slugify(topic)
    # Determine next lesson number by scanning existing lesson folders
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../lessons'))
    existing = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
    numbers = [int(re.split('[-_]', d)[0]) for d in existing if re.match(r'\d+', d)]
    next_num = max(numbers, default=0) + 1
    lesson_dir = os.path.join(base_path, f"{next_num:02d}-{slug}")
    os.makedirs(lesson_dir, exist_ok=True)
    
    # Placeholder for LLM generation
    en_desc = outline if outline else f"Introduction to {topic}."
    zh_desc = f"{topic} 的简介。"
    
    # Files to generate
    files = {
        'README.md': f"# Lesson {next_num:02d}: {topic}\n\n## Bilingual Content (Side‑by‑Side)\n\n| 🇺🇸 English | 🇨🇳 中文 |\n| :--- | :--- |\n| **Concept:** | **概念：** |\n| {en_desc} | {zh_desc} |\n",
        'handout.md': f"# Handout – Lesson {next_num:02d}\n\n> 🇺🇸 English summary: Learn the basics of {topic}.\n> 🇨🇳 中文摘要: 学习 {topic} 的基础知识。\n",
        'exercise.md': f"# Exercise – Lesson {next_num:02d}\n\n- **Task:** Practice the concepts of {topic}.\n- **Submission:** Link to your GitHub repo in the support chat.\n",
        'rubrics.md': "# Rubric\n\n| Criterion | Points | Description |\n| :--- | :---: | :--- |\n| Logic/Accuracy | 10 | Correct implementation of {topic}. |\n| Quality | 10 | High-quality prompt/code. |\n"
    }
    for name, content in files.items():
        with open(os.path.join(lesson_dir, name), 'w') as f:
            f.write(content)
    print(f"Lesson created at {lesson_dir}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lesson Generator Skill prototype')
    parser.add_argument('--topic', required=True, help='High‑level lesson topic')
    parser.add_argument('--milestone', help='Milestone identifier')
    args = parser.parse_args()
    create_lesson(args.topic, args.milestone)
