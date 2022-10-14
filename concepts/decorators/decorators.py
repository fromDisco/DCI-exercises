def outer(name):
    print("i am outer")
    def inner():
        print(f"i {name} am inner")

    return inner

outer("Mi")()

print(outer)


# division case
def check_divisor(func):
    def inner(a, b):
        if b == 0:
            print("You cannot divide by 0")
            return
        return func(a,b)
    return inner

def divide(a, b):    
    return a / b

print("\n# DECORATOR")
divide = check_divisor(divide)
print(divide(4, 2))
print(divide(4, 0))


def make_title(func): # we expect the function to return a string
    def inner(string):
        return f"Mr. {func(string).title()}"

    return inner        

@make_title
def greetings(greet):
    return greet

print(greetings("fausto doe"))