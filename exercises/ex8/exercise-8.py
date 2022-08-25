def find_nemo(string):
    if string.find("Nemo") != -1:
        return "I found Nemo at " + str(string.find("Nemo"))
    else:
        return "I can't find Nemo :("


print(find_nemo("I am finding Nemo!"))
print(find_nemo("Nemo is me"))
print(find_nemo("Hello World"))
