import random

def display_menu():
    print("\n--- Quiz Application ---")
    print("1. Start Quiz")
    print("2. View Instructions")
    print("3. Exit")

def display_instructions():
    print("\nInstructions:")
    print("- Each question has four options.")
    print("- Type the letter corresponding to your answer (e.g., 'a', 'b', 'c', 'd').")
    print("- You will get 1 point for each correct answer.")
    print("- Try to get the highest score!\n")

def get_questions():
    return [
        {
            "question": "Who developed Python Programming Language?",
            "options": ["a. Wick van Rossum", "b. Rasmus Lerdorf", "c. Guido van Rossum", "d. Niene Stom"],
            "answer": "c"
        },
        {
            "question": "Which type of Programming does Python support?",
            "options": ["a. object-oriented programming", "b. structured programming", "c. functional programming", "d. all of the mentioned"],
            "answer": "d"
        },
        {
            "question": "Which of the following is the correct extension of the Python file?",
            "options": ["a. .python", "b. .pl", "c.  .py", "d. a & b"],
            "answer": "d"
        },
        {
            "question": "Python supports the creation of anonymous functions at runtime, using a construct called __________",
            "options": ["a. pi", "b. anonymous", "c. lambda", "d. none of the mentioned"],
            "answer": "c"
        },
        {
            "question": " What does pip stand for python?",
            "options": ["a. Pip Installs Python", "b. Pip Installs Packages", "c. Preferred Installer Program", "d. All of the mentioned"],
            "answer": "c"
        }
    ]

def start_quiz():
    questions = get_questions()
    random.shuffle(questions)
    score = 0

    print("\nStarting the quiz! Answer carefully.\n")

    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("Your answer: ").lower()
        if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Quiz completed! Your score is {score}/{len(questions)}.\n")
    return score

def main():
    high_score = 0
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            score = start_quiz()
            if score > high_score:
                high_score = score
                print(f"Congratulations! You've set a new high score: {high_score}\n")
            else:
                print(f"Your score: {score}. High score: {high_score}\n")
        elif choice == "2":
            display_instructions()
        elif choice == "3":
            print("Thank you for using the Quiz Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
