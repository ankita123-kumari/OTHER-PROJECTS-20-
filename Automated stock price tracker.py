import tkinter as tk
from tkinter import messagebox
import yfinance as yf

# Function to get stock price
def get_stock_price():
    stock_symbol = entry.get().strip().upper()
    if not stock_symbol:
        messagebox.showwarning("Warning", "Please enter a stock symbol!")
        return
    
    try:
        stock = yf.Ticker(stock_symbol)
        price = stock.info["regularMarketPrice"]
        messagebox.showinfo("Stock Price", f"Current price of {stock_symbol}: ${price:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch stock price.\n{e}")

# GUI Setup
root = tk.Tk()
root.title("AI-Powered Stock Price Tracker")

tk.Label(root, text="Enter Stock Symbol (e.g., AAPL, TSLA):").pack(pady=10)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

tk.Button(root, text="Get Stock Price", command=get_stock_price).pack(pady=10)

root.mainloop()