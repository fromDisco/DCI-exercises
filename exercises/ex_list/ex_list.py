# Exercise
# To get a total, we have a function that looks like this, rewrite (refactor) the function to use a while loop

def total_list(lst):
    total = 0
    for item in lst:
        total += item
    return total


# test case
# print(total_list([1,2,3]))   # answer is 6


def total_list1(lst):
    total = 0
    i = 0
    while i < len(lst):
        total += lst[i]
        i += 1
        
    return total


# test case
# print(total_list1([1,2,3]))   # answer is 6


# while loop: print the following word: "You are 10kg"
counter = 0
weight = ['10kg', '20kg', '30kg']
while counter < len(weight): # 99% # false !    
    print(weight[counter])
    counter += 1

colors = ["red", "green", "yellow"]
while True:
    if colors[i] == "red":
        print("I love red")
        break
