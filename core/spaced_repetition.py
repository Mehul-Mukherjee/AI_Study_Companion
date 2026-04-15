"""
Spaced Repetition Engine (Simple Rule-Based Version)

This module decides when a topic should be reviewed again
based on the learner's mastery score.
"""

def next_review(mastery: float) -> str:
    """
    Returns recommended review interval based on mastery level.

    Args:
        mastery (float): Average mastery score between 0 and 1

    Returns:
        str: Human-readable time interval for next review
    """

    if mastery < 0:
        mastery = 0.0
    if mastery > 1:
        mastery = 1.0

    if mastery < 0.3:
        return "1 day"
    elif mastery < 0.6:
        return "3 days"
    elif mastery < 0.8:
        return "7 days"
    else:
        return "14 days"