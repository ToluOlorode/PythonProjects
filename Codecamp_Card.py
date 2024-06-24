# codeacademy notes

def main():
    card_number = '4111-1111-4555-1142'
    card_translation= str.maketrans({'-': '', ' ': ''}) # str maketrans replaces characters
    translated_card_number = card_number.translate(card_translation)
    
    #print(translated_card_number)
    if verify_card_number(translated_card_number):
        print("VALID!")
    else:
        print("INVALID!")


def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed =card_number[::-1] #card_number[0:4:2] # only access from index 0-4 and every second digit between the 0-4 #card_number[-1:-5:-1] - reversed and sliced
    #print(card_number_reversed)
    odd_digits = card_number_reversed[::2] #contains every other digit from the reversed variable
    
    for digits in odd_digits:
        sum_of_odd_digits += int(digits)# convert the string into an integer

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2] # even digits
    for digits in even_digits:
            number = int(digits) * 2
            if number >= 10:
                number = number // 10 + number % 10
            sum_of_even_digits += number
    
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    
    return 0 == total % 10

main()
