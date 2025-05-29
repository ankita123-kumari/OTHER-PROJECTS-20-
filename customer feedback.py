import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database setup
conn = sqlite3.connect("customer_feedback.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        comments TEXT
    )
""")
conn.commit()

# Function to submit feedback
def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    comments = text_comments.get("1.0", "end-1c")

    if not name or not email or not comments:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    cursor.execute("INSERT INTO feedback (name, email, comments) VALUES (?, ?, ?)", (name, email, comments))
    conn.commit()
    messagebox.showinfo("Success", "Feedback submitted successfully!")
    entry_name.delete(0, "end")
    entry_email.delete(0, "end")
    text_comments.delete("1.0", "end")

# GUI Setup
root = tk.Tk()
root.title("Customer Feedback System")

tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.pack(pady=5)

tk.Label(root, text="Comments:").pack(pady=5)
text_comments = tk.Text(root, width=50, height=10)
text_comments.pack(pady=5)

tk.Button(root, text="Submit Feedback", command=submit_feedback).pack(pady=10)

root.mainloop()