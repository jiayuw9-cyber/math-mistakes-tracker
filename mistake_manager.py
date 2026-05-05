#1. add_mistake
#Allows the user to input a math problem and save the wrong answer and correct answer.
#This function saves math mistakes into a text file.
def add_mistake(filename):
    question = input("Enter the math problem you got wrong (e.g., 5 + 3): ").strip()
    wrong_answer = input("Enter the math question:").strip()
    correct_answer = input("enter the correct answer:").strip()

    if question == "" or wrong_answer == "" or correct_answer == "":
        print("Error: All fields are required. Please try again.")
        return

    with open (filename,"a") as file:
        file.write(question + " | " + wrong_answer + " | " + correct_answer + "\n")
    
    print("Mistakes saved successfully.")


#2. load_mistakes
#Put the data out of file.
def load_mistakes(filename):
    mistakes = []

    try:
        with open(filename,"r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split(" | ")

                if len(parts) == 3:
                    question = parts[0]
                    wrong_answer = parts[1]
                    correct_answer = parts[2]
                    mistakes.append((question, wrong_answer, correct_answer))

    except FileNotFoundError:
        print ("No file found.")  
    return mistakes   

#3. view_mistakes
#Displays all stored mistakes for review.
def view_mistakes(filename):
    mistakes = load_mistakes(filename)

    if len(mistakes) == 0:
        print("No mistakes recorded yet.")
        return
    
    print ("Saved Math Mistakes.")

    for i in range(len(mistakes)):
        mistake = mistakes[i]
        question = mistake[0]
        wrong_answer = mistake[1]
        correct_answer = mistake[2]

        print(f"\nMistake {i+1}")
        print(f"Question: {question}")
        print(f"Your wrong answer: {wrong_answer}")
        print(f"Your correct answer: {correct_answer}")
    
