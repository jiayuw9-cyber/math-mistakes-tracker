import random
from mistake_manager import load_mistakes 

# split it into three parts
def save_mistakes(filename, mistakes):
    with open(filename, "w") as file:
        for question, wrong_answer, correct_answer in mistakes:
            file.write(question + " | " + wrong_answer + " | " + correct_answer + "\n")


def quiz_user(filename):
    mistakes = load_mistakes(filename)

    if len(mistakes) == 0:
        print("There are no mistakes to quiz.")
        return

    num_questions = min(10, len(mistakes))
    selected = random.sample(mistakes, num_questions)

    still_wrong = []

    for i in range(len(selected)):
        mistake = selected[i]
        question, wrong_answer, correct_answer = mistake

        print(f"\nQuestion{i}:{question}")
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer.strip():
            print("Correct!")
        else:
            print(f"Wrong. Correct answer: {correct_answer}")
            still_wrong.append(mistake)

    not_selected = []

    for mistake in mistakes:
        if mistake not in selected:
             not_selected.append(mistake)

    updated_mistakes = not_selected + still_wrong
    save_mistakes(filename, updated_mistakes)

    print("\nQuiz finished!")
