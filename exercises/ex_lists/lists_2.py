def full_name(*args): # "tuple"
    # 2 names, 3 etc.
    # Handle it "gracefully!!"
    # print(args)
    # return f"{args[0]} {args[1]} {args[2]} {args[3]}"
    # --> TUPLE / List (Tuples cannot be changed/mutated )
    collected = ""
    for names in args:
        if names != args[-1]:
            collected += f"{names} "
        else: 
            collected += f"{names}"

    return collected


# andres felipe castro salazar
output = full_name("Felipe", "Dr.", "jr.", "jr.", "jr.", "jr.", "Gonzalez")
# print(output)
# print(full_name(input("First name "), input("Last name")))

try:
    print(int("Hey"))
except ValueError:
    pass