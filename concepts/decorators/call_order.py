def decor1(func):
    def wrap():
        print("1************")
        func()
        print("i am first")
        print("2************")

    return wrap


def decor2(func):
    def wrap():
        print("1@@@@@@@@@@@@")
        func()
        print("i am second")
        print("2@@@@@@@@@@@@")

    return wrap


@decor1
@decor2
def sayhellogfg():
    print("Hello")
    return


# def saygfg():
# print("GeekforGeeks")
# return

# sayhellogfg()
# saygfg()


def decorator1(func):
    def wrap(*args, **kwargs):
        kwargs["cat_says"] = "meow"
        return func(*args, **kwargs)

    return wrap


def decorator2(func):
    def wrap(*args, **kwargs):
        print(kwargs.pop("cat_says"))
        return func(*args, **kwargs)

    return wrap


class C:
    @decorator1
    @decorator2
    def spam(self, a, b, c, d=0):
        print("Hello, cat! What's your favourite number?")
        return a + b + c + d


x = C()
print(x.spam(1, 2, 3, d=7))
