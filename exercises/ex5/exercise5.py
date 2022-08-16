# print("\n---TASK 7--- \n")
# print('* ',2 * '* ', 3 * '* ', 4 * '* ', sep='\n')
# n=5
# for i in range(n, 0, -1):
#     for j in range(i):
#         print('* ', end="")
#     print('')
# 

# 0, 1, 1, 2, 3, 5, 8
x, y = 0, 1
while y < 50:
    print(y)
    x, y = y, x + y
