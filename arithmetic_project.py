def arithmetic_arranger(problems, show_answers=False):

    # Variables
    solutions = []
    first_row = "" 
    last_row = ""
    dashes = ""
    answer_row = ""

    # Error One - Length
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Error Two - Operators
    operators = []
    for problem in problems:
        maths = problem.split()
        operators.append(maths[1])

    for operator in operators:
        if operator in ["*", "/"]:
            return "Error: Operator must be '+' or '-'."
    
    # Error Three - Digits
    numbers = []
    for problem in problems:
        maths = problem.split()
        numbers.append(maths[0])
        numbers.append(maths[2])

    for number in numbers:
        if not number.isdigit():
            return "Error: Numbers must only contain digits."
        # Error Four - Operand Length
        elif len(number) > 4:
            return "Error: Numbers cannot be more than four digits."

    for i in range(0, len(numbers), 2):
        num1 = int(numbers[i])
        num2 = int(numbers[i + 1])
        operator = operators[i // 2]

        if operator == "+":
            result = num1 + num2
        else:
            result = num1 - num2
        solutions.append(result)

        # Format Rows
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        first_row += numbers[i].rjust(space_width)
        last_row += operator + numbers[i + 1].rjust(space_width - 1)
        dashes += "-" * space_width

        # Space between Problems
        if i != len(numbers) - 2:
            first_row += " " * 4
            last_row += " " * 4
            dashes += " " * 4

    # Format Answers
    for i in range(len(solutions)):
        space_width = max(len(numbers[2 * i]), len(numbers[2 * i + 1])) + 2
        answer_row += str(solutions[i]).rjust(space_width)
    
        # Answer Spaces
        if i != len(solutions) - 1:
            answer_row += " " * 4
        
    # Return
    if show_answers:
        arranged_problems = "\n".join((first_row, last_row, dashes, answer_row)) 
    else:
        arranged_problems = "\n".join((first_row, last_row, dashes))

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
