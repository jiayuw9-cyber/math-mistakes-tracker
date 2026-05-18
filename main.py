#import
from mistake_manager import add_mistake, view_mistakes
from quiz import quiz_user

filename = "mistakes.txt"

#show menu
def main():
      while True:
            print("\n Math Mistakes Tracker")
            print("1. Add mistakes")
            print("2. View mistakes")
            print("3. Quiz yourself")
            print("4. Quit")

            choice = input("Choose an option:")

            if choice == "1":
                  question = input("Enter the math problem: ")
                  wrong_answer = input("Enter your wrong answer: ")
                  correct_answer = input("Enter the correct answer: ")
                  
                  add_mistake(
                        question,
                        wrong_answer,
                        correct_answer,
                        filename
                  )
                  
            elif choice == "2":
                  view_mistakes(filename)

            elif choice == "3":
                  quiz_user(filename)

            elif choice == "4":
                  print("End.")
                  break
            else:
                  print("Invalid choice. Plz write the number 1, 2, 3, 4.")

if __name__ == "__main__":
      main()