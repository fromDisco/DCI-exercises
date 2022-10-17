def outer():
    def inner():
        print(inner)




def outer(x):
    def add_mr_miss(y):
        return f'Mr/Ms {y}'
    return add_mr_miss(x)

print(outer('Doe'))


# passing a function as an argument

def do_something(string, func):
    return func(string)

def add_a_greeting(name):
    return "Good morning " + name

def make_upper(name):
    return name.title()

print(do_something('peer', make_upper))
print(do_something('peer', add_a_greeting))