import customtkinter as ctk
import tkinter as tk
import json
import os
from tkinter import simpledialog, messagebox

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            for task in json.load(f):
                tasks_box.insert(tk.END, task)

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(list(tasks_box.get(0, tk.END)), f)

def add_task():
    task = entry.get().strip()
    if task:
        tasks_box.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Empty", "Type a task to add.")

def update_task():
    sel = tasks_box.curselection()
    if sel:
        current = tasks_box.get(sel)
        new = simpledialog.askstring("Update Task", "Edit:", initialvalue=current)
        if new:
            tasks_box.delete(sel)
            tasks_box.insert(sel, new.strip())
            save_tasks()

def delete_task():
    sel = tasks_box.curselection()
    if sel:
        tasks_box.delete(sel)
        save_tasks()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("To-Do List")
root.geometry("400x480")

ctk.CTkLabel(root, text="To-Do List", font=ctk.CTkFont(size=28, weight="bold")).pack(pady=(18, 10))

tasks_box = tk.Listbox(root, width=50, height=15, font=("Segoe UI", 14), bd=2, relief="flat", selectbackground="#3894fc")
tasks_box.pack(pady=8)

entry = ctk.CTkEntry(root, width=220, font=ctk.CTkFont(size=14), placeholder_text="Add a new task...")
entry.pack(pady=10)

btn_frame = ctk.CTkFrame(root, fg_color="transparent")
btn_frame.pack(pady=8)
ctk.CTkButton(btn_frame, text="Add", width=70, command=add_task).grid(row=0, column=0, padx=5)
ctk.CTkButton(btn_frame, text="Update", width=70, command=update_task).grid(row=0, column=1, padx=5)
ctk.CTkButton(btn_frame, text="Delete", width=70, fg_color="#e74c3c", hover_color="#c0392b", command=delete_task).grid(row=0, column=2, padx=5)

load_tasks()
root.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), root.destroy()))
root.mainloop()
