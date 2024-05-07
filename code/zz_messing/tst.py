# plottask.py
# Author: Matthias Wiedemann
# As per weekly task 8 this is a program that displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.
# The course material from week 8 has also provided some useful information in working this out.

# First of all plot libraries numpy and matplotlib.pyplot have to be imported.

import numpy as np
import matplotlib.pyplot as plt

# Second, we need 1000 random values (or an array of 1000 random numbers from a normal Gaussian distribution) 
# with mean of 5 and standard deviation of 2 in normal distribution.
# My research brought to the very Numpy.org documentation:
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# random.normal(loc=0.0, scale=1.0, size=None). The code at the bottom of the page helped me to figure out what value goes where in the code parameter.

random = np.random.normal(5, 2, 1000)

# Plot histogram: I looked the code up on: https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/
# I used this code initially:
'''
plt.hist(random)  
'''
# Then tried the code as proposed in above link, the result looks much nicer: 

plt.hist(random, bins=30, color='green', edgecolor='black')

# Adding labels and title, again just used what is proposed in above link.

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Normal distribtion')

# Display the plot

plt.show()

# Plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes: I am currently doing a bit of research on this.
# https://www.geeksforgeeks.org/plot-mathematical-expressions-in-python-using-matplotlib/

# Defining function h(x) = x^3 (x to the power of 3)

x = np.linspace(0, 10)  # np.linspace: Return evenly spaced numbers over a specified interval (this task requires 0 to 10). Very handy function, here I got it from above link
y = x**3                # y equals a number between 0 and 10 to the power of 3.

# Plotting x & y

plt.plot(x, y) 

# Playing around with x & y limits
# Default limits of x & y are defined with linspace 0 t 10, if I manually define the limits as per below, the graph would end in the center of the plot
# Why? Highest possible value would be 10 to the power of 3: 10 * 10 * 10 = 1000

plt.xlim(0, 20)
plt.ylim(0, 2000)

# Adding titles and labels to horizontal & vertical axis

plt.title('h(x)=x3 in the range 0 to 10')
plt.xlabel('value')
plt.ylabel('h(x)=x3')
plt.grid(True)             # Adding grid. More infos here: https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python

# Show plot
plt.show()

# I figured out that if I use the plt.show() command only once at the end of the program it produces histogram and plot in one single image:

random = np.random.normal(5, 2, 1000)

plt.hist(random, bins=30, color='skyblue', edgecolor='black')

plt.xlabel('Values')                # Labels & title won't show in this version, only the ones defined for the plot which comes next.
plt.ylabel('Frequency')
plt.title('Normal distribtion')

x = np.linspace(0, 10)
y = x**3   

plt.plot(x, y) 

plt.xlim(0, 10)
plt.ylim(0, 1000)

plt.title('h(x)=x3 in the range 0 to 10')
plt.xlabel('value')
plt.ylabel('h(x)=x3')
plt.grid(True)

plt.show()

