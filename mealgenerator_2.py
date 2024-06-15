import random

### Empty list
meals = []

## Question
print("******** Random Meal Generator ********")
print("Don't know what to eat? Let us decide for you!")
print("But first! You need to input what meals you currently have!")


# Add Meals

def addfood():
    food = True
    
    while food:
        addmeal = input("What Food Would You Like To Add? ")
        if addmeal:
            meals.append(addmeal)
        else:
            print("You can't eat an empty list! Please input something.")
        
        again = input("\nDo you want to add more? (yes/no) ").strip().lower()
        if again == "no":
            food = False

addfood() 

if not meals:
    print("No meals were added. Closing the Generator! ")
else:
## Main Loop
    while True:
        ### User Input
        user = input("Type 'random' for a random meal or 'exit' to leave: ").strip().lower()
    
        if user.lower() == 'random':
            selections = random.choice(meals)
            print(f"Your random meal is: {selections}")
        elif user == 'exit':
            print("Thank you for using the Random Meal Generator. See you next time!")
            break
    
        else:
            print("Please only input random or exit.")

        repeat = input("Would you like another choice? (yes/no): ").strip().lower()
        if repeat == 'no':
            print("Thank you for using the Random Meal Generator! I hope it was useful!")
            break
        elif repeat != "yes":
            print("Uhh.... Exiting the Generator")
            break
    
