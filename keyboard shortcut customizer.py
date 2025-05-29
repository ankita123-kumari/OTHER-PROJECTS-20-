import tkinter as tk
from tkinter import messagebox
import keyboard

# Dictionary to store shortcuts
shortcuts = {}

# Function to add shortcut
def add_shortcut():
    action = entry_action.get().strip()
    key = entry_key.get().strip()

    if not action or not key:
        messagebox.showwarning("Warning", "Please enter both action and key!")
        return

    shortcuts[key] = action
    keyboard.add_hotkey(key, lambda: messagebox.showinfo("Shortcut Triggered", f"Action: {action}"))
    messagebox.showinfo("Success", f"Shortcut '{key}' set for '{action}'")

# GUI Setup
root = tk.Tk()
root.title("Keyboard Shortcut Customizer")

tk.Label(root, text="Enter Action:").pack(pady=5)
entry_action = tk.Entry(root, width=30)
entry_action.pack(pady=5)

tk.Label(root, text="Enter Shortcut Key (e.g., ctrl+shift+a):").pack(pady=5)
entry_key = tk.Entry(root, width=30)
entry_key.pack(pady=5)

tk.Button(root, text="Add Shortcut", command=add_shortcut).pack(pady=10)

root.mainloop()