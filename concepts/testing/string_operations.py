# - Write a function to make two names titlezed e.g. title_name(name1, name1)
def titlelize(name1: str, name2: str):
    return name1.capitalize(), name2.capitalize()


# - write a function, when given a list of names, 
# it creates one name (test it too) e.g. join_names([‘name1’, ‘name2’, ‘name3’])
def unite_names(name_list):
    return " ".join(name_list)

