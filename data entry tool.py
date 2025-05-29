import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database setup
conn = sqlite3.connect("data_entry.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT
    )
""")
conn.commit()

# Function to submit data
def submit_data():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()

    if not name or not email or not phone:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    cursor.execute("INSERT INTO entries (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    messagebox.showinfo("Success", "Data submitted successfully!")
    entry_name.delete(0, "end")
    entry_email.delete(0, "end")
    entry_phone.delete(0, "end")

# GUI Setup
root = tk.Tk()
root.title("Data Entry Tool")

tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.pack(pady=5)

tk.Label(root, text="Phone:").pack(pady=5)
entry_phone = tk.Entry(root, width=40)
entry_phone.pack(pady=5)

tk.Button(root, text="Submit Data", command=submit_data).pack(pady=10)

root.mainloop()