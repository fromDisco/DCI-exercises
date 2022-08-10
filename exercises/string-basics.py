city = "London"
print(city)

city2 = "Berlin"
population = 3645000
print(city2 + ": " + str(population))

city3 = "London"
population3 = 900000

str = "city: {city} ({bool}) \nPopulation: {population}"
output = str.format(city=city3, population=population3, bool=city3.isalpha())
print(output)

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
index = text.index("capital")
print("capital: " + str(index))