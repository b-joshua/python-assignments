import random
import tkinter as tk
from tkinter import messagebox

def start_new_game():
    global rand_num, attempts
    rand_num = random.randint(1, 20)
    attempts = 0
    entry.delete(0, tk.END)
    status_label.config(text="Guess a number between 1 and 20.")

def make_guess():
    global attempts
    user_input = entry.get()
    if not user_input.isdigit():
        status_label.config(text="Please enter a valid number.")
        return

    guess = int(user_input)

    if not (guess > 0) & (guess < 21):
        status_label.config(text="Please enter a number between 1 and 20.")
        return
    
    attempts += 1

    if guess < rand_num:
        status_label.config(text="Your guess was too low. Try again!")
    elif guess > rand_num:
        status_label.config(text="Your guess was too high. Try again!")
    else:
        messagebox.showinfo("Correct!", f"The number was {rand_num}! It took you {attempts} attempts to guess.")
        if messagebox.askyesno("Play Again?", "Do you want to play again?"):
            start_new_game()
        else:
            root.quit()

# Initialize the main window
root = tk.Tk()
root.title("Guessing Game")

# Initialize game variables
rand_num = random.randint(1, 20)
attempts = 0

# Create widgets
label = tk.Label(root, text="Guess a number between 1 and 20:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=make_guess, bg="lightgreen", fg="black")
guess_button.pack(pady=5)

new_game_button = tk.Button(root, text="New Game", command=start_new_game, bg="lightblue", fg="black")
new_game_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit", command=root.quit, bg="red", fg="black")
quit_button.pack(pady=5)

status_label = tk.Label(root, text="", fg="black")
status_label.pack(pady=10)

# Start the main event loop
root.mainloop()