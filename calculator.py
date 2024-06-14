def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        print("You can't divide by 0")
    else:
        return x/y

#Main Cal Loop

while True:
    print("--------------------")
    print("\nSelect Options:")
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Multiply")
    print("4. Divide ")
    print("EXIT")
    print("--------------------")
    
    selection = input("\nWhat would you like to do today? '(1-4) or EXIT': ")
    
    if selection in ("1,2,3,4"):
        number1 = float(input("Input your first number: "))
        number2 = float(input("Input your second number: "))
        
        if selection == "1":
            print(number1, "+", number2, "=", add(number1, number2))
        elif selection == "2":
            print(number1, "-", number2, "=", subtract(number1, number2))
        elif selection == "3":
            print(number1, "*", number2, "=", multiply(number1, number2))
        elif selection == "4":
            print(number1, "/", number2, "=", divide(number1, number2))
        
    elif selection == "EXIT":
            print("Calculator Cancelled!")
            break
        
    else:
        print("\nPlease select from the options above!")
