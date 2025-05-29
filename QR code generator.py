import tkinter as tk
from tkinter import filedialog, colorchooser
import qrcode
from PIL import Image, ImageTk
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Function to generate QR code
def generate_qr():
    data = entry.get()
    if not data:
        result_label.config(text="Please enter text or URL!")
        return
    
    filename = filename_entry.get() or "qr_code"
    fg_color = fg_color_var.get()
    bg_color = bg_color_var.get()

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    img.save(f"{filename}.png")

    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)

    qr_label.config(image=img)
    qr_label.image = img
    result_label.config(text=f"QR Code Saved as {filename}.png")

# Function to choose foreground color
def choose_fg_color():
    color = colorchooser.askcolor()[1]
    if color:
        fg_color_var.set(color)

# Function to choose background color
def choose_bg_color():
    color = colorchooser.askcolor()[1]
    if color:
        bg_color_var.set(color)

# Function to scan QR code
def scan_qr():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_data.set(f"Scanned Data: {obj.data.decode('utf-8')}")
            cap.release()
            cv2.destroyAllWindows()
            return
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator & Scanner")

tk.Label(root, text="Enter text or URL:").pack()
entry = tk.Entry(root, width=40)
entry.pack()

tk.Label(root, text="Save as (filename):").pack()
filename_entry = tk.Entry(root, width=40)
filename_entry.pack()

fg_color_var = tk.StringVar(value="black")
bg_color_var = tk.StringVar(value="white")

tk.Button(root, text="Choose Foreground Color", command=choose_fg_color).pack()
tk.Button(root, text="Choose Background Color", command=choose_bg_color).pack()

tk.Button(root, text="Generate QR Code", command=generate_qr).pack()

result_label = tk.Label(root, text="")
result_label.pack()

qr_label = tk.Label(root)
qr_label.pack()

tk.Button(root, text="Scan QR Code", command=scan_qr).pack()
qr_data = tk.StringVar()
qr_data_label = tk.Label(root, textvariable=qr_data)
qr_data_label.pack()

root.mainloop()