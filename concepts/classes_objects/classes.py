class Person:
    test_thing = "I am here"

    def __init__(self, name, address): 
        self.name = name
        self.address = address
    # functions within classes are called methods.
    def talk_about_yourself(self):
        return f"Hi, my name is {self.name}. I live in {self.address}"


# instance (object)    
# instantiation ! 
shaban = Person('Shaban', 'Berlin')
names = ['shaban', 'jacques', 'peer']
locations = ['Berlin', 'Hamburg', 'Munich']

collection = []
for name, location in zip(names, locations):
    collection.append(Person(name, location))
#print(collection)

talk_about_self = [instance.talk_about_yourself() for instance in collection]
#print(talk_about_self)

crisu = Person("crisu", "da")
michel = Person("michel", "hier")
print("Crisu before change:", crisu.test_thing)

michel.test_thing = "Personal change for Michel"
print("\nMichel after personal change:", michel.test_thing)
print("No change for Crisu:", crisu.test_thing)

# changes the attribute for every object
Person.test_thing = "changed"
print("\nMichel was not changed")
print("Michel after global change:", michel.test_thing)
print("Crisu after global change:", crisu.test_thing)











