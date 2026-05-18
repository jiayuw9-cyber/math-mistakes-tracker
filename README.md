# Math Mistakes Tracker

## Project Discription 

The program allows users to record math problems they got wrong and review them later. 

Users can store：
1. the math question
2. their incorrect answer
3. their correct answer.

The program also includes a quiz function that can randomly selects recorded mistakes. 

---

## Code Structure

### gui.py  
GUI version of the project.  
Allows users to add mistakes, view mistakes, and complete quizzes using tkinter.

### main.py  
Provides a text-based menu for adding mistakes, viewing mistakes, and taking quizzes.

### mistake_manager.py  
Handles all mistake management functions including:
- adding mistakes
- loading mistakes
- viewing mistakes
- saving mistakes to the text file

### quiz.py  
Contains the quiz system logic.  
Randomly selects questions from the mistake list and removes correctly answered questions from the file.

### test_file.py  
Unit testing file using unittest.  

### mistakes.txt  
Stores all saved math mistakes.

---

## Functions

### add_mistake
Allows the user to input a math problem and save the wrong answer and correct answer.
This function saves math mistakes into a text file.

### view_mistakes
Displays all stored mistakes for review.

### quiz
Randomly selects a stored question and quizzes the user.


## Installation
Make sure you have python installed on your computer.

---

## How to Run:
Run gui.py is recommended.

Run GUI version:

```bash
python gui.py
```

Run tests:

```bash
python test_file.py
```
This is only used to test the core functions.

---

## Example
Example of stored data in mistakes.txt.

1+1 | 3 | 2

4 + 5 = ? | 3 | 9

15 + 27 = ? | 40 | 42  

---

## Input Data Format

The program uses a text file (mistakes.txt) to stored data.

Each line follows this format:

```text
question | wrong_answer | correct_answer
```

All values are store as strings when loaded from the file.

---

## Example Use Cases

1. Students can review their mistakes to improve accuracy.
2. Teachers can track common errors made by students.
3. Users can generate quizzes from past mistakes for practice.
