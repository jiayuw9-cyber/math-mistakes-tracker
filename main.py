#import
from mistake_manager import add_mistake, view_mistakes
from quiz import quiz_user, plot_recent_results

# I using ai here for debugging as 
def add_mistake(problem, wrong_answer, correct_answer, filename):
    with open(filename, "a") as file:
        file.write(f"{problem}//{wrong_answer}//{correct_answer}\n")


filename = "mistakes.txt" ##??

#show menu
def main():
      while True:
            print("\n Math Mistakes Tracker")
            print("1. Add mistakes")
            print("2. View mistakes")
            print("3. Quiz yourself")
            print("4. Plot recent quiz results")
            print("5. Quit")

            choice = input("Choose an option:")

            if choice == "1":
                  problem = input("Enter the math problem: ")
                  wrong_answer = input("Enter your wrong: ")
                  correct_answer = input("Enter your correct answer: ")

                  add_mistake(problem, wrong_answer, correct_answer, filename) ##??
                  print("Mistakes added succesfully.")

            elif choice == "2":
                  view_mistakes(filename)

            elif choice == "3":
                  quiz_user(filename)

            elif choice == "4":
                  plot_recent_results()

            elif choice == "5":
                  print("End.")
                  break
            else:
                  print("Invalid choice. Plz write the number 1, 2, 3, 4, 5.")


if __name__ == "__main__":
      main()