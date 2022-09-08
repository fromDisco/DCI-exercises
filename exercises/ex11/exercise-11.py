import re
# TODO: try regex


def replace_dog(string, old, new):
    return string.replace(old, new)


sentence = "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."
old = " dog "
new = " cat "
print(replace_dog(sentence, old, new))
