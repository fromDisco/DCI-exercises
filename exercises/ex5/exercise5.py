# Task 1
print("--- Task 1 ---")

def user_promt():
    """
        ask user to input three values
    """

    first = int(input("First number, please: "))
    second = int(input("Second number, please: "))
    third = int(input("Third number, please: "))

    return first, second, third


def calc(num1, num2, num3):
    """
        if all numbers are equal, sum all and triple the result
        otherwise just calculate the sum of all numbers
    """

    result = num1 + num2 + num3
    result = result * 3 if num1 == num2 == num3 else result # overwrite result

    return result


# user_nums = user_promt()
# print(calc(*user_nums))


# Task 2
print("--- Task 2 ---")

def user_input():
    first = int(input("First number: "))
    second = int(input("Second number: "))
    
    return first, second


def difference(num1, num2):
    result = num1 - num2

    if result > 0:
        result = result * 2
    else:
        result = abs(result)

    return "The result is " + str(result)


# two_numbers = user_input()
# print(difference(*two_numbers))



# Task 3
print("--- Task 3 ---")


def odd_or_even(num):
    result = "even" if num % 2 == 0 else "odd"
    txt = f"{num} is an {result} number"
    return txt
    

print(odd_or_even(10))



# Task 4
print("--- Task 4 ---")
from math import pi 


def circle_area(radius):

    area = round(pi * radius ** 2, 2)
    return area


# print(circle_area(3.45))



# Task 5
print("--- Task 5 ---")
# its an useless complicated solution
# but it was a good exercise for recursion 
to_guess = 8


def user_guess():
    guess = int(input("Guess from 1 to 9: "))
    return comparison(guess)


def comparison(guess):
    while guess != to_guess:
        print("Sorry. Wrong number. Try again.")
        return user_guess()
    
    # is executed once, if guess is correct
    return "Well guessed: " + str(guess) 


# print(user_guess())



# Task 6
print("--- Task 6 ---")


def celsius_fahrenheit(temp, scale):
    if scale == "C":
        result = (temp * 1.8) + 32
    elif scale == "F":
        result = (temp - 32) / 1.8

    return result


def temp_input():
    temperatur = int(input("What is the temperature to convert: "))
    scale = input("What is the scale Shortcut (F or C): ")

    return temperatur, scale


# user_temps = temp_input()
# print(celsius_fahrenheit(*user_temps))


# Task 7
print("--- Task 7 ---")


def print_pattern():
    top = "*", "*"*2, "*"*3
    return top
    

print(print_pattern())