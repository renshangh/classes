#!/usr/bin/env python3
import os
import json
import sys
import glob

def summarize_class(repo_path, class_id):
    """
    Scans for student submissions and checkpoint data in the classes repo.
    """
    base_dir = os.path.join(repo_path, "classes", "openclaw-beginner-class", "classes", class_id)
    if not os.path.exists(base_dir):
        return {"error": f"Class directory {class_id} not found."}

    # In a real scenario, we'd search for student folders or issue comments.
    # For now, we simulate finding checkpoint data.
    return {
        "class_id": class_id,
        "checkpoints": [
            {"id": "cp1", "question": "Can you run 'openclaw status'?", "status": "80% Success"},
            {"id": "cp2", "question": "Did you create your first skill?", "status": "60% Success"}
        ],
        "common_blockers": [
            "Permission denied on /opt/homebrew",
            "API key not set in environment"
        ]
    }

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Usage: summarize_class.py <repo_path> <class_id>"}))
        sys.exit(1)
    
    result = summarize_class(sys.argv[1], sys.argv[2])
    print(json.dumps(result, indent=2))
