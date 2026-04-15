import json
import os

DATA_PATH = "data/progress.json"


def load_data():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r") as f:
        return json.load(f)


def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)


def update_progress(topic, score):
    data = load_data()

    if topic not in data:
        data[topic] = []

    data[topic].append(float(score))

    save_data(data)
    return data