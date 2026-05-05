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
    mistakes = load_mistkes(filename)
    text.delete("1.0", tk.END)

    if not mistakes:
        text.insert(tk.END, "No mistakes.\n")
        return
    
    for i in range(len(mistakes)):
        q = 

