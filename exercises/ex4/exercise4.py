# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

# Task 1
print("--- TASK 1 ---")

def comparison(num1, num2):

    # Did user provide both values?
    if num1 and num2:
        print("Both values were given.")

    # Because a string of non-integer value will throw
    # an error in int(), catch that error
    try:
        if int(num1) and int(num2):
            print("Both values were valid")
            # If both values are integers convert from str to int
            num1 = int(num1)
            num2 = int(num2)
    except: 
        print("At leat one value was invalid")
        # If error stop the whole function
        return "Please try again"
        
    # Are both values equal?   
    if num1 == num2:
        print("Both values are equal.")

    # Is num1 bigger than num2
    if num1 > num2:
        print(f"{num1} is bigger than {num2}")

    # Is num1 smaller than num2
    if num1 < num2:
        print(f"{num1} is smaller than {num2}")

    # check which number is even or odd
    num1_even = True if (num1 % 2 == 0) else False
    num2_even = True if (num2 % 2 == 0) else False

    # print out which one is even or odd
    if num1_even and num2_even:
        print("Both numbers are even")
    elif not(num1_even) and not(num2_even):
        print("Both numbers are odd.")
    elif num1_even:
        print(f"{num1} is even.")
    elif num2_even:
        print(f"{num2} is even.")
        

    if not(num1_even):
        print(f"{num1} is odd")

    if not(num2_even):
        print(f"{num2} is odd")
    

# ask for user input
def user_input():
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")

    # start the party
    comparison(number1, number2)


user_input()


def days_in_month(month):
    print(month)
    

def user_month(month_list):
    print(month_list)    


month_list = {
    "January": 31,
    "February": 28,
}