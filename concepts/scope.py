first_name = "Green"

def full_name():
    # first_name = "Flower"
    last_name = "Blossom"
    # if variable is declared inside the function its local
    # if variable is only declared outside, function uses global variable
    print(first_name)
    print("id INNER: ", id(first_name))


full_name()
print("id OUTER: ", id(first_name))