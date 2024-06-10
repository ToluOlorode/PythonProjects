## Welcome Users
print("----------------")
name = input("\nWhat is your name?: ")

print(f"Welcome {name} to your To Do List! ")
print("\nPlease select from the Options below :) ")

print("----------------")


## Add Task

todo_tasks = []

def addtask():
    tasks = True
    
    while tasks:
        todo = input("\nWhat Tasks will you like to add? ")
        todo_tasks.append(todo)
        
        repeat = input("Do you have another Task to add? 'Yes / No'?: ")
        if repeat.lower() == 'no':
            tasks = False

##Show Tasks

def showtasks():
    if not todo_tasks:
        print("\nYour List is Empty! Please add to your list")
    else:
        for todo in todo_tasks:
            print(f"Your Current To-Do List Contains: {todo.title()}")
        

## Mark Task as Done

def taskdone():
    if not todo_tasks:
        print("\nYour ToDo List is empty... Consider adding something? ")
    else:
        print(f"\n{name}'s ToDo List:")
        for index, todo in enumerate(todo_tasks, start=1):
            print(f"{index}. {todo.title()}")
            
        completed_task = int(input("\nWhat Number Task would you like removed? "))
        if 1 <= completed_task <= len(todo_tasks):
            completed_task = todo_tasks.pop(completed_task - 1)
            print(f"The Task '{completed_task.title()}' has been removed from your list!")
        else:
            print("Unable to remove any Tasks, Please enter a number from 1 to the number of Tasks in your list.")
            
    

### Options to select from

def main():
    
    tasks_active = True
    while tasks_active:
        print("\nTo-Do List")
        print("1. Add Task ")
        print("2. Show Task ")
        print("3. Mark Task as Done")
        print("4. Exit")
        
        choice = input("Please select your choice! '(1-4)': ")
        
        if choice == '1':
            addtask()
        elif choice == "2":
            showtasks()
        elif choice == '3':
            taskdone()
        elif choice == "4":
            print("\nYou have exited out of your todo list! ")
            break
        
if __name__ == "__main__":
    main()
