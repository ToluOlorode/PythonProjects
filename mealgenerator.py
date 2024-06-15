import random

### List of Meals
meals = ["Jollof Rice", "Tikka Massala", "Pounded Yam", "Noodles", "Pizza"]

## Question
print("******** Random Meal Generator ********")
print("Don't know what to eat? Let us decide for you!")


## Main Loop

while True:
    ### User Input
    user = input("Type 'random' for a random meal: ").strip().lower()
    
    if user.lower() == 'random':
        selections = random.choice(meals)
        print(f"Your random meal is: {selections}")
    
    else:
        print("Please only input random.")
    
    repeat = input("Would you like another choice? (yes/no): ").strip().lower()
    if repeat == 'no':
        print("Thank you for using the Random Meal Generator! I hope it was useful!")
        break
