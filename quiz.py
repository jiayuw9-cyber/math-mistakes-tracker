import random
from mistake_manager import load_mistakes 
import matplotlib.pyplot as plt

result_file = "quiz_result"
# split it into three parts
def save_mistakes(filename, mistakes):
    with open(filename, "w") as file:
        for question, wrong_answer, correct_answer in mistakes:
            file.write(question + " | " + wrong_answer + " | " + correct_answer + "\n")

def save_quiz_result(accuracy):
    with open(result_file,"a") as file:
            file.write(str(accuracy) + "\n")
# ensure save in result_file

def load_quiz_results():
    results = []

    try:
         with open(result_file, "r") as file:
              for line in file:
                   line = line.strip()
                   if line != "":
                        results.append(float(line))

    except FileNotFoundError:
         return[]
    
    return results


def quiz_user(filename):
    mistakes = load_mistakes(filename)

    if len(mistakes) == 0:
        print("There are no mistakes to quiz.")
        return
    
# Random choose 10 mistakes
    num_questions = min(10, len(mistakes))
    selected = random.sample(mistakes, num_questions)

    score = 0
    still_wrong = []
#just show the question
#make user print the answer 
    for i, mistake in range(len(mistakes)):   #????
        question, wrong_answer, correct_answer = mistake

        print(f"\nQuestion{i}:{question}")
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer.strip():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Correct answer: {correct_answer}")
            still_wrong.append(mistake)

#keep mistakes which were not seected and the selected questions that are still wrong.
    not_selected = []

    for mistake in mistakes:
        if mistake not in selected:
             not_selected.append(mistake)

    updated_mistakes = not_selected + still_wrong
    save_mistakes(filename, updated_mistakes)

    accuracy = score / num_questions
    save_quiz_result(accuracy)

    print("\nQuiz finished!")
    print(f"Score: {score}/{num_questions}")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("The question you answered correctly has already remved from the mistakes list!")


#show the conclusion as a line plot.
def plot_recent_results():
    results = load_quiz_results()

    if len(results) == 0:
        print("No quiz results to plot.")
        return
    
    recent_results = results[-10:]

    x_values = list(range(1,len(recent_results) + 1))
    y_values = [result * 100 for result in recent_results]

    plt.plot(x_values, y_values, marker = "o")
    plt.xlabel("Recent Quiz Attempts")
    plt.ylabel("Accuracy (%)")
    plt.title("Recent Quiz Accuracy")
    plt.ylim(0,100)
    plt.show()