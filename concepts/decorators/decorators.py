import inspect


def greeting():
    return "Hey"


no = greeting

print(greeting)
print(inspect.getsource(greeting))