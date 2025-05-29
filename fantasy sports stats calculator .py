import tkinter as tk
from tkinter import messagebox
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Yahoo Fantasy API setup
API_KEY = "your_yahoo_api_key"
BASE_URL = "https://fantasysports.yahooapis.com/fantasy/v2/player/"

# Function to fetch player stats
def get_player_stats(player_name):
    try:
        response = requests.get(f"{BASE_URL}{player_name}?apikey={API_KEY}")
        data = response.json()
        stats = data["fantasy_content"]["player"]["player_stats"]
        return pd.DataFrame(stats)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch player stats.\n{e}")
        return None

# Function to compare teams
def compare_teams():
    team1 = entry_team1.get().strip()
    team2 = entry_team2.get().strip()
    
    if not team1 or not team2:
        messagebox.showwarning("Warning", "Please enter both team names!")
        return
    
    team1_stats = get_player_stats(team1)
    team2_stats = get_player_stats(team2)
    
    if team1_stats is not None and team2_stats is not None:
        plt.figure(figsize=(8, 5))
        plt.plot(team1_stats["points"], label=team1, marker="o")
        plt.plot(team2_stats["points"], label=team2, marker="s")
        plt.xlabel("Games")
        plt.ylabel("Fantasy Points")
        plt.title("Team Comparison")
        plt.legend()
        plt.show()

# GUI Setup
root = tk.Tk()
root.title("Fantasy Sports Stats Calculator")

tk.Label(root, text="Enter Team 1 Name:").pack(pady=5)
entry_team1 = tk.Entry(root, width=30)
entry_team1.pack(pady=5)

tk.Label(root, text="Enter Team 2 Name:").pack(pady=5)
entry_team2 = tk.Entry(root, width=30)
entry_team2.pack(pady=5)

tk.Button(root, text="Compare Teams", command=compare_teams).pack(pady=10)

root.mainloop()