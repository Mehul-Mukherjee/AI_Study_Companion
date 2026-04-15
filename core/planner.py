from core.knowledge_model import compute_mastery
from core.spaced_repetition import next_review


def generate_study_plan(data):
    plan = {}

    for topic in data:
        mastery = compute_mastery(topic, data)
        review = next_review(mastery)

        plan[topic] = {
            "mastery": round(mastery, 2),
            "next_review": review
        }

    return plan