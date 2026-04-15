📚 AI Study Companion v2
AI-Powered Adaptive Learning & Study Intelligence System

🚀 Overview
AI Study Companion v2 is an intelligent EdTech system that goes beyond a simple tracker. It models learning behavior, identifies weak topics, generates adaptive quizzes, and builds personalized revision schedules using spaced repetition principles.
Unlike static learning dashboards, this system behaves like a lightweight AI tutor that continuously adapts to user performance.

🎯 Key Features
📊 1. Learning Progress Intelligence


Tracks topic-wise performance over time


Stores historical scores for trend analysis


Computes dynamic mastery score per topic



🧠 2. Adaptive Quiz Engine


Generates contextual quiz questions per topic


Supports conceptual + analytical question types


Detects math-like topics for deeper reasoning prompts



📅 3. Personalized Study Planner


Converts performance into actionable study schedules


Assigns revision intervals using spaced repetition logic


Prioritizes weak topics automatically



🔁 4. Spaced Repetition System


Implements adaptive review cycles:


Low mastery → frequent revision


High mastery → delayed reinforcement





🧩 5. Modular AI Architecture
Clean separation of concerns:


core/ → learning intelligence engine


app/ → UI layer (Streamlit)


utils/ → storage + helper logic


data/ → persistent learning state



🏗️ Project Structure
AI_Study_Companion_v2/│├── app/│   ├── ui.py                  # Streamlit dashboard│   ├── main.py                # CLI entry (optional)│├── core/│   ├── knowledge_model.py     # Mastery computation engine│   ├── tracker.py             # Progress tracking system│   ├── quiz_engine.py         # Adaptive quiz generation│   ├── planner.py             # Study plan generator│   ├── spaced_repetition.py   # Review interval logic│├── ai/│   ├── llm_client.py          # (Optional) LLM integration layer│   ├── prompts.py             # Prompt templates│├── utils/│   ├── storage.py             # JSON persistence layer│├── data/│   ├── progress.json          # Learning history database│├── requirements.txt└── README.md

⚙️ Installation
1. Clone Repository
git clone git@github.com:Mehul-Mukherjee/AI_Study_Companion.gitcd AI_Study_Companion

2. Create Virtual Environment (Recommended)
python -m venv venvsource venv/bin/activate   # macOS/Linux

3. Install Dependencies
pip install -r requirements.txt

▶️ Running the Application
📌 Streamlit UI (Recommended)
streamlit run app/ui.py

📌 CLI Mode (Optional)
python -m app.main

🧪 How It Works
1. Add Learning Data
User enters:


Topic


Score (0–1)


System stores:
maths → [0.7, 0.5, 0.9]

2. Mastery Computation
mastery = average(score history per topic)

3. Study Plan Generation
System maps mastery → revision schedule:
Mastery LevelReview Interval< 0.31 day0.3–0.63 days0.6–0.87 days> 0.814 days

4. Quiz Generation
System dynamically generates:


Conceptual questions


Application-based questions


Reasoning-based prompts



🧠 Design Philosophy
This project is built on 3 principles:
1. Learning is a time-series problem
Performance improves when tracked over time, not in isolation.
2. Weakness-driven adaptation
The system prioritizes reinforcement of weak topics.
3. Simple architecture > over-engineering
Modular design allows easy upgrade into ML/LLM systems.

📈 Future Improvements


🔥 LLM-powered quiz generation (Groq / OpenAI)


📊 Visualization dashboard (learning curves)


🧠 ML-based difficulty prediction


👤 Multi-user authentication system


📱 Mobile-friendly UI


☁️ Deployment (Streamlit Cloud / AWS)



🛠️ Tech Stack


Python 3.10+


Streamlit


JSON-based persistence


Modular architecture design


(Optional) Groq / LLM APIs



⚠️ Security Note


.env files are excluded via .gitignore


API keys must never be committed


Sensitive data is stored locally only



👨‍💻 Author
Mehul Mukherjee
AI / Software Engineering Projects
GitHub: https://github.com/Mehul-Mukherjee

⭐ If You Like This Project
If you're reviewing this repo, consider:


⭐ starring the repository


🧠 exploring the architecture


🔧 suggesting improvements



