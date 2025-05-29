import tkinter as tk
from tkinter import messagebox
import torch
from diffusers import StableDiffusionPipeline

# Load Stable Diffusion model
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.to("cuda")  # Use GPU if available

# Function to generate image
def generate_image():
    prompt = entry.get()
    if not prompt:
        messagebox.showwarning("Warning", "Please enter a prompt!")
        return
    
    image = pipe(prompt).images[0]
    image.save("generated_image.png")
    messagebox.showinfo("Success", "Image generated and saved as 'generated_image.png'!")

# GUI Setup
root = tk.Tk()
root.title("AI-Powered Image Generator")

tk.Label(root, text="Enter a prompt for image generation:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Generate Image", command=generate_image).pack(pady=10)

root.mainloop()