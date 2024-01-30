# floaterry.py
# Author: Andrew Beatty
# A simple program to demonstrate that 
# floating point aritmetic is not exact 
# (this is for most(all) programming languages)

floatnum = 0.29

ascent = floatnum*100

print (f"{ascent}")
# prints 28.999999999999996

'''
n = 100
for i in range(0, n + 1):
  a = int(100 * (float(i) / 100))
  if i != a: print (i, a)
'''