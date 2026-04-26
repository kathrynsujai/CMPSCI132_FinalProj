#Final Project

#import the random method
import random
rand_num = random.randint(1,100)
print("Welcome to the Number Guessing Game! You will have 7 attempts to guess a number from 1 to 100.")
attempt_lim = 7
attempt = 0
status = False

while attempt < attempt_lim:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        player_guess = int(guess)
    else:
        print("Please enter a number.")
        guess = input("Enter your guess: ")

    attempt += 1
    
    if player_guess > rand_num:
        print("Too high!")
    elif player_guess < rand_num:
        print("Too low!")
    else:
        print(f"Correct! You guessed it in {attempt} attempts!")
        status = True
        attempt = attempt_lim

if not status:
    print(f"Sorry, you're out of attempts. The number was {rand_num}.")
    
        

    
