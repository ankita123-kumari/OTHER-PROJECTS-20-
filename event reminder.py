import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import smtplib
import schedule
import time
import threading

# Database setup
conn = sqlite3.connect("event_reminders.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event TEXT,
        date TEXT,
        time TEXT,
        email TEXT
    )
""")
conn.commit()

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_password"

# Function to send email notification
def send_email(recipient_email, event):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        message = f"Subject: Event Reminder\n\nReminder: {event}"
        server.sendmail(SENDER_EMAIL, recipient_email, message)
        server.quit()
        print(f"Email sent to {recipient_email} for event: {event}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to add reminder
def add_reminder():
    event = entry_event.get()
    date = entry_date.get()
    time_ = entry_time.get()
    email = entry_email.get()

    if not event or not date or not time_ or not email:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    cursor.execute("INSERT INTO reminders (event, date, time, email) VALUES (?, ?, ?, ?)", (event, date, time_, email))
    conn.commit()
    messagebox.showinfo("Success", "Reminder added successfully!")
    entry_event.delete(0, "end")
    entry_date.delete(0, "end")
    entry_time.delete(0, "end")
    entry_email.delete(0, "end")

# Function to check reminders
def check_reminders():
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        cursor.execute("SELECT event, email FROM reminders WHERE date || ' ' || time = ?", (now,))
        reminders = cursor.fetchall()
        for event, email in reminders:
            messagebox.showinfo("Reminder", f"Event Reminder: {event}")
            send_email(email, event)
        time.sleep(60)  # Check every minute

# Start reminder checker in background
threading.Thread(target=check_reminders, daemon=True).start()

# GUI Setup
root = tk.Tk()
root.title("Event Reminder System")

tk.Label(root, text="Event Name:").pack(pady=5)
entry_event = tk.Entry(root, width=40)
entry_event.pack(pady=5)

tk.Label(root, text="Date (YYYY-MM-DD):").pack(pady=5)
entry_date = tk.Entry(root, width=40)
entry_date.pack(pady=5)

tk.Label(root, text="Time (HH:MM):").pack(pady=5)
entry_time = tk.Entry(root, width=40)
entry_time.pack(pady=5)

tk.Label(root, text="Email for Notification:").pack(pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.pack(pady=5)

tk.Button(root, text="Add Reminder", command=add_reminder).pack(pady=10)

root.mainloop()