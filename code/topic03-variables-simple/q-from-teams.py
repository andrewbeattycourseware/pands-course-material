# this is some code that I am reproducing from a question from teams
# inputs should return a string
# author: Andrew Beatty

# this does not work because later I try to add a integer to number (number needs to be an int)
#number = input("please enter a number:")

# this reads in the number and convert it to an int
number = int(input("please enter a number:"))

newnumber = number + 1

# old way of doing formatting not best practice
print (str(number)+" plus one is "+ str(newnumber))

# better way of doing formating
print(f"{number} plus one is {newnumber}")