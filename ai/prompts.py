# -----------------------------
# QUIZ PROMPT
# -----------------------------
QUIZ_PROMPT = """
You are an expert teacher.

Create a quiz for the topic: "{topic}"

Rules:
- Difficulty: {difficulty}
- Generate 5 questions
- Mix conceptual + practical questions
- Do NOT give answers
- Format clearly as numbered list
"""


# -----------------------------
# STUDY PLAN PROMPT
# -----------------------------
PLAN_PROMPT = """
You are an AI learning planner.

Given this student progress data:
{progress_data}

Task:
- Identify weak topics
- Create a 7-day structured study plan
- Include daily focus areas
- Suggest revision intervals
- Keep it concise and actionable

Format:
Day 1:
Day 2:
...
"""