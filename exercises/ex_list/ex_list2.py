# To get a total, we have a function that looks like this, rewrite (refactor) the function to use a while loop
# def total_list(lst):
#     total = 0
#     for item in lst:
#         total += item
#     return total
# # test case
# print(total_list([1,2,3]))   # answer is 6
def total_list(lst):
    l = 0
    total = 0
    while l < len(lst):
       total += lst[l]
       l += 1

    return total
print(total_list([3,9,8]))
# con = ['Iran', 'Germany', 'Britain']
# for c in con:
    # con += con
    # print(con)
def country(con):
    cont += cont[l]
    l = 0
    while l < len(con):
        l = l + 1
        cont += con[l]
        print(cont)
        l += 1
        return f'I love {cont}'
# print(country(['Iran', 'Germany', 'Britain']))