# This is some code that I am reproducing from a question from teams.
# Inputs should return a string (and do for me)
# Author: Andrew Beatty

# This input returns a string and causes the later line to throw an error (tyring to add an integer to a string)
#number = input("please enter a number:")

# This reads in the input and converts it to an integer
number = int(input("please enter a number:"))

# if the type of number is a string then this will throw an error
newnumber = number + 1

# old way of doing formatting, not best practice
print (str(number)+" plus one is "+ str(newnumber))

# better way of doing formating
print(f"{number} plus one is {newnumber}")