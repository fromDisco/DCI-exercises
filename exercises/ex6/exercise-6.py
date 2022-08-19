# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
# task1

three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 5
max_num = 100

for i in range(1, max_num):
    # % or modulo division gives you the remainder

    if i % num1 == 0 and i % num2 == 0:
        print(i, three_mul + five_mul)
    elif i % num1 == 0:
        print(i, three_mul)
    elif i % num2 == 0:
        print(i, five_mul)


# task2
n = [0, 1, 2, 3, 4, 5]
num1 = 0
summ = 0

while n < n + 1:
    summ = num1 + n
    num1 = num1 + 1
print("Sum =", summ)

# Task 4
# 4.1
for a in range(3):
    print(a)

#
x = 10
while x > 0:
    print(x)
    x -= 1
