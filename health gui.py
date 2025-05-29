import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to add health data
def add_health_data():
    date = entry_date.get()
    weight = entry_weight.get()
    steps = entry_steps.get()

    if not date or not weight or not steps:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    conn = sqlite3.connect("health_tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO health_data (date, weight, steps) VALUES (?, ?, ?)", (date, weight, steps))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Health data added successfully!")
    entry_date.delete(0, "end")
    entry_weight.delete(0, "end")
    entry_steps.delete(0, "end")

# GUI Setup
root = tk.Tk()
root.title("Health Tracker")

tk.Label(root, text="Date (YYYY-MM-DD):").pack(pady=5)
entry_date = tk.Entry(root, width=30)
entry_date.pack(pady=5)

tk.Label(root, text="Weight (kg):").pack(pady=5)
entry_weight = tk.Entry(root, width=30)
entry_weight.pack(pady=5)

tk.Label(root, text="Steps:").pack(pady=5)
entry_steps = tk.Entry(root, width=30)
entry_steps.pack(pady=5)

tk.Button(root, text="Add Health Data", command=add_health_data).pack(pady=10)

root.mainloop()