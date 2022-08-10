# Write a program that detects if a string has an even/odd number of 
# characters and prints "even" or "odd" accordingly.

def odd_or_not(sentence):
    return "even" if len(sentence) % 2 == 0 else "odd"

print(odd_or_not("hello world"))
