import streamlit as st

from core.tracker import update_progress, load_data
from core.knowledge_model import compute_mastery
from core.planner import generate_study_plan
from core.quiz_engine import generate_quiz


st.set_page_config(page_title="AI Study Companion v2", layout="centered")

st.title("📚 AI Study Companion v2")
st.subheader("Track Your Learning (AI-powered)")


data = load_data()

# -----------------------------
# UPDATE PROGRESS
# -----------------------------
st.header("📊 Update Learning Progress")

topic = st.text_input("Topic")
score = st.number_input("Score (0 to 1)", min_value=0.0, max_value=1.0, step=0.1)

if st.button("Update Progress"):
    update_progress(topic, score)

    data = load_data()

    mastery = compute_mastery(topic, data)
    plan = generate_study_plan(data)

    st.success("Progress updated!")

    st.write("### Mastery")
    st.write(mastery)

    st.write("### Study Plan")
    st.json(plan)


# -----------------------------
# QUIZ SECTION
# -----------------------------
st.header("🧠 Quiz Generator")

quiz_topic = st.text_input("Quiz Topic")

if st.button("Generate Quiz"):
    questions = generate_quiz(quiz_topic)

    for q in questions:
        st.write("•", q)