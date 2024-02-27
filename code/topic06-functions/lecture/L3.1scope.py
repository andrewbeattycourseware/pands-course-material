# more messing with functions
# variable scope
# Author: Andrew Beatty

# I don't want you to use global variables

x = 999

def fun(num):
    print(num)

def fun2(x2):
    print(f"in fun2 x {x2}")
    x = 21
    print(f"in fun2 x {x2}")
    
    

fun2(x)
print(f"after fun2 x is {x}")