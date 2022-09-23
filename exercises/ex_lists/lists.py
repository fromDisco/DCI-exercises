names = ["Victor", "Peter", "Mary", "John", "Badara", "Peer"]
# 
# using an index, replace "Peer" with "Malcom X"

# Add two names to the list of names

# Experiment with the methods in a list using dir(names)

print(names)

print("\n# names[-1] = 'Malcom X':")
names[-1] = "Malcom X"
print(names)

names.append("Wojciech")
print("\n# names.append('Wojciech')")
print(names)

add_this = ["Nadja", "BamBam", "SheRa", "Orco"]
names.extend(add_this)
print("\n# names.extend(add_this):")
print(names)

to_be_replaced = names.index("BamBam")
names[to_be_replaced] = "Grisu"
print("\n# names[to_be_replaced] = 'Grisu'")
print(names)

names.remove("John")
print("\n# names.remove('John')")
print(names)

names[0] = "badara"
print("\n# names[0] = 'badara'")
print(names)

names[:0] = ["Test"]
print("\n# names[:0] = ['Test'], -> if not in Brackets, string is split into chars")
print(names)

names.insert(0, "ThereIsNoGod")
print("\n# names.insert(0, 'ThereIsNoGod')")
print(names)