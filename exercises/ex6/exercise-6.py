# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
#task1
three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 5 
max_num = 100
   
for i in range(1,max_num):
    # % or modulo division gives you the remainder 
    
    if i%num1 == 0 and i%num2 == 0:
        print(i, three_mul+five_mul)
    elif i%num1 == 0:
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)

#task2

n = [0,1,2,3,4,5]
number = 0
sum = 0
while n <  n+ number:
    sum = number + n
    number = number + 1
print("Sum =", sum)

# Task 4
x = 10
while x > 0:
    print(x)
    x -= 1
    