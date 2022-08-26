def inator(word):
    vowels = "aeiou"
    length = str(len(word)) + "0" * 3

    if vowels.find(word[-1]) != -1:
        return word + "-inator " + str(length)
    else:
        return word + "inator " + str(length)


print(inator("Shrink"))
print(inator("Clone"))
