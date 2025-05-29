import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to organize files
def organize_files():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        messagebox.showwarning("Warning", "Please select a folder!")
        return
    
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Audio": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"]
    }

    for file in os.listdir(folder_path):
        file_ext = os.path.splitext(file)[1]
        for category, extensions in file_types.items():
            if file_ext in extensions:
                category_folder = os.path.join(folder_path, category)
                if not os.path.exists(category_folder):
                    os.mkdir(category_folder)
                shutil.move(os.path.join(folder_path, file), category_folder)

    messagebox.showinfo("Success", "Files organized successfully!")

# GUI Setup
root = tk.Tk()
root.title("AI-Powered File Organizer")

tk.Label(root, text="Select a folder to organize:").pack(pady=10)
tk.Button(root, text="Organize Files", command=organize_files).pack(pady=10)

root.mainloop()