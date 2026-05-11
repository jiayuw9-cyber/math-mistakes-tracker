Math Mistakes Tracker
Project Discription: 
The program will allow users to record math problems they got wrong and review them later. 
Users can store the question, their incorrect answer, and the correct answer. 
The program will also include a quiz function that can randomly selects recorded mistakes. 

Functions:
1. add_mistake
Allows the user to input a math problem and save the wrong answer and correct answer.
This function saves math mistakes into a text file.

2. view_mistakes
Displays all stored mistakes for review.

3. quiz
Randomly selects a stored question and quizzes the user.

Installation:
Make sure you have python installed on your computer.

How to Run:
[IMPORTANT] Run gui.py instead of run the test_file.py.
            Run test_file.py can just test the core functions work or not.

Example
Example of stored data in mistakes.txt.
1+1 | 3 | 2
4 + 5 = ? | 3 | 9
15 + 27 = ? | 40 | 42  

Input Data Format:
The program uses a text file (mistakes.txt) to store data.
Each line follows this format:
question | wrong_answer | correct_answer
All values are store as strings whn loaded from the file.

Example Use Cases:
1. Students can review their mistakes to improve accuracy.
2. Teachers can track common errors made by students.
3. Users can generate quizzes from past mistakes for practice.
