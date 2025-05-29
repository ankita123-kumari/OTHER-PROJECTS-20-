import tkinter as tk
from tkinter import messagebox
import openai

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

# Function to generate recipe suggestions
def generate_recipe(ingredients):
    prompt = f"Suggest a recipe using the following ingredients: {ingredients}. Provide step-by-step instructions."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Function to display recipe
def get_recipe():
    ingredients = entry.get()
    if not ingredients:
        messagebox.showwarning("Warning", "Please enter some ingredients!")
        return
    
    recipe = generate_recipe(ingredients)
    messagebox.showinfo("Recipe Suggestion", recipe)

# GUI Setup
root = tk.Tk()
root.title("AI-Powered Recipe Suggestion")

tk.Label(root, text="Enter ingredients (comma-separated):").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Get Recipe", command=get_recipe).pack(pady=10)

root.mainloop()