import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice
def play_game():
    user_choice = entry.get().strip().lower()
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    full_user_choice = choices.get(user_choice, user_choice)
    
    if full_user_choice not in choices.values():
        result_label.config(text="Invalid choice. Please enter r, p, s, or the full name.", fg='red')
        return

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(full_user_choice, computer_choice)
    result_label.config(text=f"You chose: {full_user_choice.capitalize()}\nComputer chose: {computer_choice.capitalize()}\n{result}", fg='blue')

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")
root.configure(bg='#f7f7f7')

title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 18, "bold"), bg='#f7f7f7', fg='#333333')
title_label.pack(pady=20)

instruction_label = tk.Label(root, text="Enter your choice (r for rock, p for paper, s for scissors, or type the full name):", bg='#f7f7f7', fg='#555555')
instruction_label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 12), justify='center')
entry.pack(pady=5)

play_button = tk.Button(root, text="Play", command=play_game, font=("Helvetica", 12), bg='#4CAF50', fg='white', activebackground='#45a049')
play_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg='#f7f7f7', fg='#333333')
result_label.pack(pady=10)

footer_label = tk.Label(root, text="Enjoy the game!", font=("Helvetica", 10, "italic"), bg='#f7f7f7', fg='#888888')
footer_label.pack(side='bottom', pady=10)

root.mainloop()
