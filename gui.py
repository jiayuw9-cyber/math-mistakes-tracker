import tkinter as tk
from tkinter import messagebox
from mistake_manager import add_mistake, load_mistakes
from quiz import quiz_user

filename = "mistakes.txt"

def add():
    q = entry_q.get()
    w = entry_w.get()
    c = entry_c.get()

    if q == "" or w == "" or c == "":
        messagebox.showerror("Error","All fields required.")
        return
    
    with open(filename, "a") as f:
        f.write(q + " | " + w + " | " + c + "\n")

    messagebox.showinfo("Success","Saved!")
    entry_q.delete(0, tk.END)
    entry_w.delete(0, tk.END)
    entry_c.delete(0, tk.END)

def view():
    mistakes = load_mistakes(filename)
    text.delete("1.0", tk.END)

    if not mistakes:
        text.insert(tk.END, "No mistakes.\n")
        return
    
    for i in range(len(mistakes)):
        q = mistakes[i][0]
        w = mistakes[i][1]
        c = mistakes[i][2]

        text.insert(tk.END, f"{i+1}. {q} | Wrong: {w} | Correct: {c}\n")

def quiz():
    quiz_user(filename)


#set up the window
root = tk.Tk()
root.title("Math Mistakes Tracker")
tk.Label(root, text = "Question").pack()
entry_q = tk.Entry(root, width = 40)
entry_q.pak()

tk.Label(root, text = "Wrong Answer").pack()
entry_w = tk.Entry(root, width = 40)
entry_w.pak()

tk.Label(root, text = "Correct Answer").pack()
entry_c = tk.Entry(root, width = 40)
entry_c.pak()

tk.Button(root, text = "Add Mistake", command = add).pack()
tk.Button(root, text = "View Misakes", command = view).pack()
tk.Button(root, text = "Quiz", command = quiz).pack()

text = tk.Text(root, height = 10, width = 50)
text.pack()

root.mainloop()