import customtkinter as ctk
import random
import string
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        chars = string.ascii_letters + string.digits + string.punctuation
        pwd = ''.join(random.choice(chars) for _ in range(length))
        password_entry.configure(state="normal")
        password_entry.delete(0, ctk.END)
        password_entry.insert(0, pwd)
        password_entry.configure(state="readonly")
    except ValueError:
        messagebox.showerror("Input Error", "Enter a positive number.")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Password Generator")
root.geometry("330x200")

ctk.CTkLabel(root, text="Password Generator", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=12)

input_frame = ctk.CTkFrame(root, fg_color="transparent")
input_frame.pack(pady=5)
ctk.CTkLabel(input_frame, text="Length:").grid(row=0, column=0, padx=6)
length_entry = ctk.CTkEntry(input_frame, width=60)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12")

ctk.CTkButton(root, text="Generate", command=generate_password).pack(pady=10)

password_entry = ctk.CTkEntry(root, width=230, font=ctk.CTkFont(size=14))
password_entry.pack(pady=5)
password_entry.configure(state="readonly")

root.mainloop()
