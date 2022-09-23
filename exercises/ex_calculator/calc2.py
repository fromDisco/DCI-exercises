def calc(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "*":
        result = num1 * num2

    return result


operator_list = ["+", "-", "/", "*"]
for operator in operator_list:
    print(f"Operator: {operator}")
    print(calc(1, 4, operator))



def names(firstname, lastname="Holzky"):
    return f"First: {firstname}, Lastname: {lastname}."


print(names("Michel", "Guckmal"))


def arguments(*args):
    print(*args)


print(arguments(2, 3, 9))