# messing with ands and ors
# I recommend you do not use and/or in your programs 
# try and keep your logic as simple as possible
# Author: Andrew Beatty

# this is an invalid way of using and
# it makes no sense "and < 30" what is less than 30, ambigious 
age = 21
#if age > 18 and < 30:
#    print("you can join the army")

number = -1
# in this logic we are checking if the number is valid
if ( number >=0 ) and ( number <= 100) :
    print("valid")

# here we are checking if it is not valid (notice we use or here)
if (number <= 0) or (number >= 100 ) :
    isbad = True
    print("stop")
else:
    isbad = False
    print("go")