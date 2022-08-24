# Task 1
print("--- Task 1 ---")
city = "London"
print(city)


# Task 2
print("\n--- Task 2 ---")
city2 = "berlin"
population2 = 1000000
print(city2.capitalize() + str(population2))


# Task 3
print("\n--- Task 3 ---")
city3 = "london"
population3 = 900000
print("City: " + city3.capitalize() +
      " (" + str(isinstance(city3, str)) + ")")
print("Population: " + str(population3))


# Task 4
print("\n--- Task 4 ---")
text4 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
index4 = text4.find("capital")
print("Capital: ", index4)


# Task 5
print("\n--- Task 5 ---")
text5 = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
list5 = text5.split(" ")
print(list5)


# Task 6
print("\n--- Task 6 ---")
text6 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
newText6 = text6.replace("capital", "capital of Germany.")
print(newText6)
