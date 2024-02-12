# Messing with while loops
# Author: Andrew Beatty

#while condition:
#    statements
#
# two types
#   Counter Controled
#       we usualy use for loops for counter conttroled loops
#   Sentinal Controled
#       if you are reading in from a user, one pattern is
#       read in from the user, check the while, and then read again in the 
#       body of the while loop
# be careful of infinite loops
#   make sure you modify what you are checking 

count = 0
while (count < 10):
    print("count is ", count)
    count = count + 1

print ("at the end count is ", count)

count = 10
while count >=0:
    print ("countdown ", count)
    count -= 1
print("blast off")

# sentinal controled loop

val = input("type something (q to quit):")
while val != 'q':
    print ("hi mom")
    val = input("q to quit:")

print("all done")