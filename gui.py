import tkinter as tk
from tkinter import messagebox
from mistake_manager import add_mistake, load_mistakes
import random
from quiz import plot_recent_result
filename = "mistakes.txt"

def add():
    q = entry_q.get()
    w = entry_w.get()
    c = entry_c.get()

    if q == "" or w == "" or c == "":
        messagebox.showerror("Error","All fields required.")
        return
    
    add_mistake(q, w, c, filename)

    messagebox.showinfo("Success","Saved!")
    entry_q.delete(0, tk.END)
    entry_w.delete(0, tk.END)
    entry_c.delete(0, tk.END)

def view():
    mistakes = load_mistakes(filename)
    text.delete("1.0", tk.END)

    if len(mistakes) == 0:
        text.insert(tk.END, "No mistakes.\n")
        return
    
    for i in range(len(mistakes)):
        q = mistakes[i][0]
        w = mistakes[i][1]
        c = mistakes[i][2]

        text.insert(tk.END, f"{i+1}. {q} | Wrong: {w} | Correct: {c}\n")

def quiz():
    mistakes = load_mistakes(filename)
    if len(mistakes) == 0:
        messagebox.showinfo("Quiz","No mistakes to quiz.")
        return
    
    question, wrong, correct = random.choice(mistakes)
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz")

    tk.Label(quiz_window, text = question).pack()
    entry_q = tk.Entry(quiz_window, width = 40)
    entry_q.pack()

    def check():
        user_answer = entry_q.get().strip()
        if user_answer == correct.strip():
            messagebox.showinfo("Result","Correct!")
        else:
            messagebox.showinfo("Result",f"Wrong. Correct answer: {correct}")

        quiz_window.destroy()
    tk.Button(quiz_window, text = "Submit", command = check).pack()


#set up the window
root = tk.Tk()
root.title("Math Mistakes Tracker")
tk.Label(root, text = "Question").pack()
entry_q = tk.Entry(root, width = 40)
entry_q.pack()

tk.Label(root, text = "Wrong Answer").pack()
entry_w = tk.Entry(root, width = 40)
entry_w.pack()

tk.Label(root, text = "Correct Answer").pack()
entry_c = tk.Entry(root, width = 40)
entry_c.pack()

tk.Button(root, text = "Add Mistake", command = add).pack()
tk.Button(root, text = "View Misakes", command = view).pack()
tk.Button(root, text = "Quiz", command = quiz).pack()
tk.Button(root, text="Plot Results", command=plot_recent_result).pack()

text = tk.Text(root, height = 10, width = 50)
text.pack()

root.mainloop()