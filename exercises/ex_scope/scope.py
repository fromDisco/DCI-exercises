person = {"Name": "John", "Lastname": "aus Lönneberga", "birth_year": 1962}
# "Pass by reference" variables can change
def full_name(human):

    print("before Change: ", id(human["Name"]))
    # variations 
    human["Name"] = "Michel"
    print("whole dictionary: ", id(human))
    print("after Change: ", id(human["Name"]))
    return human

full_name(person)
print(person)