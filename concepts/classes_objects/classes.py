class Person:

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
print(collection)

talk_about_self = [instance.talk_about_yourself() for instance in collection]
print(talk_about_self)
#weißes_häkchen
#eyes
#erhobene_hände












