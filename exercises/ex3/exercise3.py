# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
def even_or_odd(number):
    """just check if parameter is even or odd"""

    if number % 2 == 0:
        #print("even number")
        return "even Number"
    else:
        # print("odd number")
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

user_input()