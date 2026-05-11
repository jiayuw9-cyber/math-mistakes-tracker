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
                  add_mistake(filename)

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