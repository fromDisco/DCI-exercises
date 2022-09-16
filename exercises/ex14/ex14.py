import re


# Create a function that takes a string input as a number and replaces leading and trailing zeros.
# 
# ## Input/Output:
# "0023.07623070"   -->   "23.0762307"  
# "hello world"     -->   "hello world"  
# "01230"           -->   "1230"  

def deleteTrailing(txt):
    print(txt)
    pattern = r"(?P<lead>^0+)|(?:\.\d*[1-9])(?P<trail>0+$)"
    in_groups = re.finditer(pattern, txt)
    for i in in_groups:
        print(i)

    

txt1 = "0023.0762307000"
txt2 = "hello world"
txt3 = "01230"
<<<<<<< HEAD
print(deleteTrailing(txt1))
=======

print(deleteTrailing(txt))
>>>>>>> 1ad15bb (moved files)
