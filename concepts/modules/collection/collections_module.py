from collections import Counter, ChainMap, OrderedDict

fridge = [
    "Apple", "Apple", "Cabbage",
    "Steak", "Cheese", "Apple",
    "Carrot", "Carrot", "Iogurt",
    "Beer"
]

# counter = Counter(fridge)
# print(counter)

counter_1 = Counter(fridge)
print("\n# counter_1")
print(counter_1)

counter_2 = Counter(Cabbage=1, Apple=1, Condoms=36)
print("\n# counter_2")
print(counter_2)

counter_1.update(counter_2)
print("\n# counter_1")
print(counter_1)

print("\n# type(counter_1)")
print(type(counter_1))


print("\n# counter_1.most_common():")
print(counter_1.most_common())


d = OrderedDict.fromkeys('abcde', 1)
print(d)