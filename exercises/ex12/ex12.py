import re


# Create a variable called `text` to store the data: `Berlin is a world city of culture, politics, media and science.` . Then search for the first white space character in the string and print its location using the appropriate label. 

# - Your result should look like this:

# The first white-space character is located at position: 6


def task1(text1):
    pattern = r"\s"
    location = re.search(pattern, text1)
    print("Returned match object from re.search():")
    print(location)
    print("\nOutput of location.span():")
    print(location.span())

    print("Location -> location.span()[0]:")
    print(location.span()[0])


print("\n---------- Task1 ----------")
text1 = "This Berlin is a world city of culture, politics, media and science." 
task1(text1)


# Create a variable called `text` to store the data: `Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.` . Then search for the word `Frankfurt` in the string . 
# 
# - Your result should look like this:
# 
# Nonehttps://stackoverflow.com/questions/66956384/how-come-vs-code-activates-the-virtualenv-automatically


def task2(text2):
    pattern = "Frankfurt"
    includes = re.search(pattern, text2)
    return includes


print("\n---------- Task2 ----------")
text2 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

print("Is 'Frankfurt' included in the string?")
print(task2(text2))




# Create a variable called `text` to store the data: `Berlin is a city of culture.` . Replace the spaces with a hyphen.
# 
# - Your result should look like this:
# 
# Berlin-is-a-city-of-culture.


def task3(text3):
    pattern = r" "
    substitutet = re.sub(pattern, "-", text3)
    return substitutet


print("\n---------- Task3 ----------")
text3 = "Berlin is a city of culture." 
print(task3(text3))


# Create a variable called `text` to store the data: `Berlin is a city of culture.` . Search if the phrase `in` appears inside the string. Print the output of the regex function.
# 
# - Your result should look like this:

# <re.Match object; span=(4, 6), match='in'>


def task4(text4):
    pattern = r"in"
    substitutet = re.search(pattern, text4)
    return substitutet


print("\n---------- Task4 ----------")
text4 = "Berlin is a city of culture." 
print("Is 'in' in here?")
print(task4(text4))


# Use the `text` variable from the previous task. Create a regular expression to look for any word that starts with an upper case "B". Print the position (start- and end-position) of the first match occurrence. 
#
# - Your result should look like this:
#(0, 6)


def task5(text4):
    pattern = r"B[a-z]+"
    which_word = re.search(pattern, text4)
    return which_word.span()



print("\n---------- Task5 ----------")
print("Is 'B' in here?")
print(task5(text4))


# Create a variable called `text` to store the data: `The rain in Spain.`. Count how many times the subphrase `ai` appears in the string. Print the results on the screen.
# 
# - Your result should look like this:
# 2


def task6(text6):
    pattern = "ai"
    counted = re.findall(pattern, text6) 
    return len(counted)


print("\n---------- Task6 ----------")
text6 = "The rain in Spain."
print("Is 'ai' in here?")
print(task6(text6))