import sys

sys.setrecursionlimit(2000)


def fact(n):
    if n == 0:
        return 1
    else: 
        return n * fact(n - 1)


print(fact(3))


for i in range(1000):
    print(fact(i), f'i->{i}')