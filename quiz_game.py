print("---------------------")
print("Welcome to my Sims 4 quiz!")
print("---------------------")

playing = input("\nDo you want to play? ")

if playing.lower() != "yes":
    quit()

print("\nOkay! Let's play :)")
score = 0

answer = input("\nWhat is the primary in-game currency used by Sims to purchase items and build houses in 'The Sims 4'? ")

if answer.lower() == "simoleons":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("\nWhat expansion introduced the ability for Sims to live in apartments and experience city life? ")

if answer.lower() == "city living":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("\nWhich of the following careers is NOT a base game career option in 'The Sims 4'? Astronaut, Entertainer, Detective or Style Influencer? ")

if answer.lower() == "detective":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat feature allows Sims to have unique personalities and affect their behavior and emotions in 'The Sims 4'? ")

if answer.lower() == "traits":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print(f"You got {score} questions correct!") # or you got + str(score) + questions correct!
print(f"You got {score / 4 * 100}%")
