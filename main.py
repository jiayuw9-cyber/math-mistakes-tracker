
#1. add_mistake
#Allows the user to input a math problem and save the wrong answer and correct answer.
#This function saves math mistakes into a text file.

def add_mistake():
question = input("Enter the math problem you got wrong (e.g., 5 + 3): ").strip()
wrong_answer = input("Enter the math question:").strip()
correct_answer = input("enter the correct answer:").strip()

if question == "" or wrong_answer == "" or correct_answer == "":
    print("Error: All fields are required. Please try again.")
    return



#2. view_mistakes
#Displays all stored mistakes for review.