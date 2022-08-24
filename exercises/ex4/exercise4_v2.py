def even_odd(string):
    return "even" if len(string) % 2 == 0 else "odd"


print(even_odd("hello world"))  # odd
print(even_odd("hello planet"))  # even
