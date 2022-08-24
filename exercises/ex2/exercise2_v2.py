# Taks 1
print("--- Task 1 ---")
text1 = "Berlin is a world city of culture, politics, media and science."
text1_length = len(text1)
print("text1 length: ", text1_length)


# Task 2
print("\n--- Task 2 ---")
text2 = "Berlin is a world city of culture, politics, media and science."
firstLastChar_text2 = text2[0] + text2[-1]
print(*firstLastChar_text2)


# Task 3
print("\n--- Task 3 ---")
text3 = "Berlin is a world city of culture, politics, media and science."
first3 = text3[:3].upper()
print(first3)


# Task 4
print("\n--- Task 4 ---")
text4 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
count4 = text4.count("B")
print("B appears", count4, "times")

# Task 5
print("\n--- Task 5 ---")
text5 = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
last10 = text5[-10:]
print("Last ten characters:", last10)

# Task 6
print("\n--- Task 6 ---")
text6 = "-----Python programming---"
stripped6 = text6.strip("-")
print(stripped6)


# Task 7
print("\n--- Task 7 ---")
firstname = "Michel"
lastname = "Holzky"
print(f"Firstname: {firstname}\nLastname: {lastname}")
