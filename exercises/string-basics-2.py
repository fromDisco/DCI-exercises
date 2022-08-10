# Task 1
print("# Task 1")
# Create a variable called text to store the data: Berlin is a world city of culture, 
# politics, media and science. . Your task is to print the length of the text variable on the screen.
text = "Berlin is a world city of culture, politics, media and science."
length = len(text)
print(length)

# Task 2
# Reuse the variable called text and print the first and the last characters on the screen.
print("# Task 2")
firstAndLast = text[0] + " " + text[-1]
print(firstAndLast)

# Task 3
# Reuse the variable called text and print the first three characters in upper case.
print("# Task 3")
firstThree = "First three characters: "  + text[0:3].upper()
print(firstThree)

# Task 4
# Create the variable called text with the following content: 
# Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, 
# Brandenburg's capital , then count how many times the letter B appears in the text.
print("# Task 4")
text2 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
occurrences = text2.count("B")
print("B appears: " + str(occurrences) + " times")

# Task 5
# Create a variable called text to store the data: 
# Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) 
# in the western borough of Spandau. . Your task is to print the last 10 characters of the text variable on screen. 
print("# Task 5")
text3 = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
lastTen = text3[len(text3) - 10:]
print(lastTen)

# Task 6
# Create a variable called text to store the data:
# ---Python programming--- . Your task is to remove the hyphen (-) character from the string.
print("# Task 6")
text4 = "---Python programming---" 
clean = text4.strip("-")
print(clean)

# Task 7
print("# Task 7")
firstName = "Michel"
lastName = "Holzky"
output = "Firstname: " + firstName + "\nLastname: " + lastName
print(output)
