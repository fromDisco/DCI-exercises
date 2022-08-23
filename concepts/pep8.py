# descriptive naming of variable and functions etc. 

# not recommended
a = 9 + 5
b = 9 - 5
c = 9 / 5
d = 9 % 5
e = 9 // 5

# better 
add = 9 + 5
subtract = 9 - 5
devide = 9 / 5
modulus = 9 % 5
int_devide = 9 // 5

# not recommended
def sb(x, y):
    z = x - y
    return z


# better
def subtraction(minuend, subtrahend):
    difference = minuend - subtrahend
    return difference 


# long lines
def much_args(argument1, argument2, argument3, argument4, argument5, argument6, argument7, argument8, argument9):
    return argument1
    

# math expressions
total = (first_var +
        second - 
        third)


result = (num1+ num2)+ ( num3 %num4+num5)-(num6)
