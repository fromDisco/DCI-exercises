# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


# Task 1
print("--- TASK 1 ---")

def even_or_odd(number):
    """just check if parameter is even or odd"""

    if number % 2 == 0:
        return "even Number"
    else:
        return "odd Number"
        

def user_input():
    """user input and distribute the incoming data"""    

    counter = 0
    while counter < 3:
        user_number = int(input("Give me number: "))
        counter += 1
        even_or_odd_answer = (even_or_odd(user_number))
        print(cap_it(even_or_odd_answer))
        

def cap_it(string):
    """capitalize the incoming string"""

    capitalized = string.upper()
    return capitalized

# user_input()


# Task 2
print("--- TASK 2 ---")

def ask_user():

    vals = {"start": 0, "stop": -1, "step": 1}

    args = int(input("How many args: "))

    if args >= 1:
       vals["stop"] = int(input("Where to stop?: ")) + 1 

    if args >= 2:
        vals["start"] = int(input("Where to start?: "))
    
    if args == 3:
        vals["step"] = int(input("Number of steps?: "))

    for i in range(*vals.values()):
        print(i)


# ask_user()




# Task 3
print("--- TASK 3 ---")

def divisors(num):

    divisor = 1 # start with one, division by 0 throw an error
    while divisor <= num: 
        if ((num / divisor) % 1 == 0): # checking if result is a whole number
            print(divisor)

        divisor += 1


divisors(24)




# Task 4
print("--- TASK 4 ---")

def is_prime(num):

    divisor_list = []
    for i in range(1, num + 1):
        if ((num / i) % 1 == 0): # checking if result is a whole number
            divisor_list.append(i) 

    if_prime = "" if divisor_list == [1, num] else "not " # decide if prime, than "", otherwise "not "

    return f"{num} is {if_prime}a prime number"


print(is_prime(89))



# Task 5
print("--- TASK 5 ---")

def fizz_buzz(num):

    fizz_string = ""
    for i in range(1, num):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


print(fizz_buzz(100))



# Task 6
print("--- TASK 5 ---")

def only_by_7(start, end):

    for i in range(start, end + 1):
        # x % 1 == 0 checks if num is an int, not a float
        if (i/7) % 1 == 0 and not (i/5) % 1 == 0:
            print(i) 

