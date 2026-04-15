def compute_mastery(topic, data):
    """
    Computes average mastery score for a topic.
    data format:
    {
        "maths": [0.7, 0.5, 0.9],
        "ml": [0.6, 0.8]
    }
    """

    scores = data.get(topic, [])

    if not scores:
        return 0.0

    return sum(scores) / len(scores)