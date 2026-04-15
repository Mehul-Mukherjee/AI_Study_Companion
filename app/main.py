from core.tracker import update_progress
from core.quiz_engine import generate_quiz
from core.planner import generate_study_plan

def run():
    print("\n📚 AI Study Companion")
    print("----------------------")

    while True:
        print("\n1. Add Score")
        print("2. Take Quiz")
        print("3. Generate Study Plan")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            topic = input("Topic: ")
            score = float(input("Score (0-1): "))
            update_progress(topic, score)
            print("Updated!")

        elif choice == "2":
            topic = input("Topic: ")
            q = generate_quiz(topic)

            if not q:
                print("No quiz found")
            else:
                print("Q:", q[0])
                ans = input("Your Answer: ")
                print("Correct Answer:", q[1])

        elif choice == "3":
            plan = generate_study_plan()
            print("\n📌 Study Plan:")
            for p in plan:
                print("-", p)

        elif choice == "4":
            break


if __name__ == "__main__":
    run()