import random

def guess(x):
    random_number = random.randint(1, x)
    
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("So close but not quite! That number is too small")
        elif guess > random_number:
            print("Sorry. That number is too big!")
    
    print("Well Done! You've guessed it correctly")
    

guess(30)
