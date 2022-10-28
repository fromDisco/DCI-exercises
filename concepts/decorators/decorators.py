import inspect

def deco(func):
    def inner(word):
        return func(word) * 2

    return inner

@deco
def greeting(word):
    return word


print(greeting("Hello"))