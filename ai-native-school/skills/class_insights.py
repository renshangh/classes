"""Class Insights Summarizer Skill (E-4) – Prototype

This script simulates the aggregation of Telegram poll data and 
GitHub support issues to provide an instructor-facing summary.

Logic:
1. Fetch latest "checkpoint" poll results.
2. Fetch GitHub issues with label "student-help" within specific milestone.
3. Generate a "Sarah Report" with comprehension rate and top blockers.
"""
import sys, argparse, json

def generate_report(lesson_id):
    # Mock data for demonstration
    mock_data = {
        "lesson": lesson_id,
        "polls": {"understood": 85, "confused": 10, "stuck": 5},
        "top_blocker": "Environment setup (Tailscale DNS)",
        "active_issues": 3
    }
    
    report = f"""
📊 Sarah's Class Insights: {mock_data['lesson']}
------------------------------------------
✅ Comprehension: {mock_data['polls']['understood']}%
🤔 Needs Detail: {mock_data['polls']['confused']}%
🛑 Stuck Now: {mock_data['polls']['stuck']}%

🔥 Top Blocker: {mock_data['top_blocker']}
📝 Active Support Tickets: {mock_data['active_issues']}

💡 Recommendation: "The Tailscale DNS step is causing friction. 
Suggest a 5-minute recap or a troubleshooting GIF in the next push."
"""
    print(report)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lesson", required=True)
    args = parser.parse_args()
    generate_report(args.lesson)
