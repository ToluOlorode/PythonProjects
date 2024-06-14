import random, sys

print("Rock, Paper or Scissors!")

wins = 0
losses = 0
ties = 0

# Main Loop
while True:
    print("%s Wins, %s Losses, %s Ties " % (wins, losses, ties))
    while True:
        print("Enter your move: Rock Paper Scissors or Quit. ")
        playermove = input()
        if playermove == 'Quit':
            sys.exit() # Quit Code
        if playermove == "Rock" or playermove == "Paper" or playermove == "Scissors":
            break # Breaks out of the Player move While Loop
        
    if playermove == "Rock":
        print("Rock versus... ")
    elif playermove == "Paper":
        print("Paper versus... ")
    elif playermove == "Scissors":
        print("Scissors versus... ")
    
    random_number = random.randint(1, 3)
    if random_number == 1:
        npcmove = "Rock"
        print("Rock")
    elif random_number == 2:
        npcmove = "Paper"
        print("Paper")
    elif random_number == 3:
        npcmove = "Scissors"
        print("Scissors")
    
    if playermove == npcmove:
        print("It is a tie!")
        ties += 1
    elif playermove == "Rock" and npcmove == "Scissors":
        print("You Win!")
        wins += 1
    elif playermove == "Paper" and npcmove == "Rock":
        print("You Win!")
        wins += 1
    elif playermove == "Scissors" and npcmove == "Paper":
        print("You Win!")
        wins += 1
    elif playermove == "Rock" and npcmove == "Paper":
        print("You Lose!")
        losses += 1
    elif playermove == "Paper" and npcmove == "Scissors":
        print("You Lose!")
        losses += 1
    elif playermove == "Scissors" and npcmove == "Rock":
        print("You Lose!")
        losses += 1
