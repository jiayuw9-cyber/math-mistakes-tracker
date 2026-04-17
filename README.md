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
Can randomly selects a stored question and quizzes the user.

Example Use Cases:
Review their math mistakes to make sure they have managed to do them.
Keep track on the types students often get wrong.
Make the mistakes together into a quiz as a kind of practice exam.

Input Data Format:
The program will use a text file for example mistakes.txt to store data as it is more conveinient for every one to do that.
All values are read as strings when loaded from the text file.
Each mistake should be stored on a seperate line.
For example:
question | wrong_answer | correct_answer
