import os
from groq import Groq
from ai.prompts import QUIZ_PROMPT, PLAN_PROMPT

load_dotenv()  

# Load API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)


# -----------------------------
# CORE CHAT FUNCTION
# -----------------------------
def chat(prompt: str, system: str = "You are an expert AI tutor.") -> str:
    """
    Generic LLM call wrapper
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content


# -----------------------------
# QUIZ GENERATION
# -----------------------------
def generate_ai_quiz(topic: str, difficulty: str = "medium") -> str:
    prompt = QUIZ_PROMPT.format(topic=topic, difficulty=difficulty)
    return chat(prompt, system="You are an AI quiz generator for students.")


# -----------------------------
# STUDY PLAN GENERATION
# -----------------------------
def generate_ai_plan(progress_data: dict) -> str:
    prompt = PLAN_PROMPT.format(progress_data=progress_data)
    return chat(prompt, system="You are a learning path optimizer.")