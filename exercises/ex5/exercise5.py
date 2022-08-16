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


two_numbers = user_input()
print(difference(*two_numbers))