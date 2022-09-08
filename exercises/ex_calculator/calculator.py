import sys


def parse():
    # is called if input comes from the command line
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    input3 = sys.argv[3]

    return input1, input2, input3


def calc(num1, num2, operator):
    try: 
        # if one of the inputs isn't a number
        # throw an error -> ValueError
        number1 = int(num1)
        number2 = int(num2)
    except ValueError:
        return "no Valid number"
    else: 
        if operator == "+":
            return number1 + number2
        elif operator == "-":
            return number1 - number2
        else:
            # if unknown or invalid operator is given
            return "no valid operator"


def input_func():
    # check if input comes from command line
    # if yes len(sys.argv) > 1
    if len(sys.argv) > 1:
        num1, num2, operator = parse() 
    else:
        # if input is not from command line, ask for input
        num1 = input("First num: ")
        num2 = input("Second num: ")
        operator = input("Which calc-method: ")

    print("\nRESULT OF:", num1, operator, num2)
    print(calc(num1, num2, operator))


input_func()