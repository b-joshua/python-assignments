import random

def game_settings(user_input, num):
    if user_input == "x":
        print("Quitting the game.")
        return 'quit'
    if user_input == "n":
        print("Starting a new game.")
        return 'new'
    if user_input == "s":
        print(f"The number is {num}")
        return 'continue'
    if user_input.isdigit() == False:
        print("Please guess a number.")
        return 'continue'

def check_guess(guess, num, attempts):
    if guess < num:
        print("Your guess was too low. Try again!")
        return False
    elif guess > num:
        print("Your guess was too high. Try again!")
        return False
    else:
        print(f"Correct! The number was {num}! It took you {attempts} attempts to guess.")
        return True
    
def replay():
    while True:
        again = input("Do you want to play again? (y/n): ")
        if again == 'y':
            print("New game!")
            return True
        elif again == 'n':
            print("Quitting")
            return False
        else:
            print("Please enter 'y' or 'n'")

def guessing_game():
    rand_num = random.randint(1, 20)
    print("Guess a number between 1 and 20.")
    attempts = 0

    while True:
        user_input = input("Enter your guess: ")
        action = game_settings(user_input, rand_num)
        if action == 'quit':
            return False
        elif action == 'new':
            return True
        elif action == 'continue':
            continue

        guess = int(user_input)
        attempts += 1

        if check_guess(guess, rand_num, attempts):
            return replay()
            
def main():
       while True:
        again = guessing_game()
        if again == False:
            break

main()