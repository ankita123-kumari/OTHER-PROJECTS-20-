import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Initialize data storage
transactions = []

# Function to add transaction
def add_transaction():
    category = category_entry.get()
    amount = amount_entry.get()
    
    if not category or not amount:
        messagebox.showerror("Error", "Please enter both category and amount.")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return
    
    transactions.append({"Category": category, "Amount": amount})
    update_display()

# Function to update display
def update_display():
    total_balance = sum(t["Amount"] for t in transactions)
    balance_label.config(text=f"Balance: ${total_balance:.2f}")
    
    transaction_text.set("\n".join([f"{t['Category']}: ${t['Amount']:.2f}" for t in transactions]))

# GUI Setup
root = tk.Tk()
root.title("Personal Finance Tracker")

tk.Label(root, text="Category:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Add Transaction", command=add_transaction).pack()

balance_label = tk.Label(root, text="Balance: $0.00", font=("Arial", 14))
balance_label.pack()

transaction_text = tk.StringVar()
transaction_label = tk.Label(root, textvariable=transaction_text, justify="left")
transaction_label.pack()

root.mainloop()