#Final Project

#import the random method
import random
rand_num = random.randint(1,100)

print("Welcome to the Number Guessing Game! You will have 7 attempts to guess a number from 1 to 100.")
print("There are three levels of diificulty, select 'easy', 'medium', 'hard'.")

d = {'easy': 10, 'medium': 7,'hard': 5}
choice = input("Choose difficulty: ")

if choice not in d:
    print("Not a valid choice, please select 'easy', 'medium', 'hard'")
    choice = input("Choose difficulty: ")
    if choice not in d:
        print("Not a valid choice, defaulting to medium")
        choice = 'medium'


attempt_lim = d[choice]

print(f"You will have {attempt_lim} attempts to guess a number from 1 to 100.")
attempt = 0
status = False

while attempt < attempt_lim:
    guess = input("Enter your guess: ")

    try:
        player_guess = int(guess)
    except ValueError:
        print("Please enter a number.")
        player_guess = None

    if player_guess is not None:
        attempt += 1
    
        if player_guess > rand_num:
            print(f"Too high! You have {attempt_lim - attempt} attempts left")
        elif player_guess < rand_num:
            print(f"Too low! You have {attempt_lim - attempt} attempts left")
        else:
            print(f"Correct! You guessed it in {attempt} attempts!")
            status = True
            attempt = attempt_lim

    if not status:
        print(f"Sorry, you're out of attempts. The number was {rand_num}.")
    
        

    
