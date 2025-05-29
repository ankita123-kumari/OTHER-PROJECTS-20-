import tkinter as tk
from tkinter import messagebox
from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization")

# Function to summarize text
def summarize_text():
    text = entry.get("1.0", "end-1c")
    if not text.strip():
        messagebox.showwarning("Warning", "Please enter some text!")
        return
    
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
    messagebox.showinfo("Summary", summary)

# GUI Setup
root = tk.Tk()
root.title("AI-Powered Text Summarizer")

tk.Label(root, text="Enter text to summarize:").pack(pady=10)
entry = tk.Text(root, width=60, height=10)
entry.pack(pady=5)

tk.Button(root, text="Summarize", command=summarize_text).pack(pady=10)

root.mainloop()