import random

def generate_quiz(topic):
    base_templates = [
        "What does {topic} represent?",
        "Explain the concept behind {topic}.",
        "Give a real-world example where {topic} is used.",
        "Why is {topic} important?",
        "What happens if {topic} is applied incorrectly?",
        "Break down {topic} step by step.",
        "How would you teach {topic} to a beginner?"
    ]

    math_templates = [
        "Solve or interpret: {topic}",
        "What assumptions are needed for {topic}?",
        "Derive a related expression from {topic}.",
        "Is {topic} always true? Explain."
    ]

    # detect math-like input
    if any(sym in topic for sym in ["=", "+", "-", "*", "/", "^"]):
        templates = base_templates + math_templates
    else:
        templates = base_templates

    selected = random.sample(templates, k=4)

    return [q.format(topic=topic) for q in selected]