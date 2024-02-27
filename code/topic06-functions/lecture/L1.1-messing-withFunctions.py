# Messing with functions
# to demonstrate the defining and using functions
# Author: Andrew Beatty

#x , y , z = (1, 2, 3)
#print (x, y, z, sep="", end="")
#print (f"{x}-{y} {z}")
#print ("{} {}--{}".format(x, y, z))

def topower(number, power=3):
    #print(number)
    return (number ** power)

#ans = topower(23)
#print(f"we got {ans}")
num = 45

print(f"and {num} is {topower(num)}")