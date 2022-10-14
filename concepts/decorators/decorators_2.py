def make_title(func):
    def inner(name):
        return func(name).title()
    return inner


def add_mr_ms(func):
    def inner(name):
        return func(f"Mr/Ms. {name}")
    return inner


@add_mr_ms
@make_title
def greetings(name):
    return name


print(greetings("fausto doe"))