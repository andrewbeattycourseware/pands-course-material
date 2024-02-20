# Messing with lists
# The code examples are in the jupyter notebook in course materials
#
# Author: Andrew Beatty
'''
boats = ['Sigma', 23, [1,2,3], {} ]

for boat in boats:
    print(type(boat))
'''
ages =[12,21,23,34, "asdfsd"]

sum = 0
'''
for age in ages:
    sum += age
print(sum)
'''
# dont do this way
'''
length_of_list = len(ages)
for i in range (0, length_of_list):
    sum += ages[i]
print (sum)
'''
'''
string = "1234567890"
print (string[6:])
'''

t = (1,2,3)
x, y, z = t
print (y)