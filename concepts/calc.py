import sys
n = len(sys.argv)
print(n)
print(sys.argv)
print('Total arguments passed:', n)
print('Name of python script:', sys.argv[0])
sum_of_arg = 0
for i in range(1, n):
    sum_of_arg += int(sys.argv[i])
print('Result:', sum_of_arg)
