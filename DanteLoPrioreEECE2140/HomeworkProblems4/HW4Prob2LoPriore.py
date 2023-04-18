import numpy as np
import matplotlib.pyplot as plt

# Dante LoPriore
# March 28, 2023
# PS4: Problem 2

# Purpose: to create a plot of two functions in range of -3/2 <= x <= 3/2, where
# y1 = sin(e^2x) and y2 = cos(e^-2x)


# initialize x limits
x_min = -3/2
x_max = 3/2
x = np.arange(x_min, x_max, 0.01)

# creating the plot representing y1 = sin(e^2x) and y2 = cos(e^-2x) in a single plot
plt.figure()
plt.plot(x, np.sin(np.exp(2*x)), 'r-', x, np.cos(np.exp(-2*x)), 'b:')
plt.grid()

# labeling the function being plotted 
plt.legend(['$y = sin(e^{2x}$)', '$y = cos(e^{-2x}$)'])
plt.ylabel('f(x)')
plt.xlabel('X')
plt.title("f(x) for Both Functions", loc='center')
plt.show()


# ploting two plots representing y1 = sin(e^2x) and y2 = cos(e^-2x) in a 2 by 1 subplot figure
plt.figure()

# plot the figure in the first row and first column of the subplot figure
plt.subplot(211)
plt.grid()

# creating the plot representing y1 = sin(e^2x) in the first row
plt.plot(x, np.sin(np.exp(2*x)), 'r-')

# labeling the function being ploted 
plt.legend(['$y = sin(e^{2x}$)'])
plt.ylabel('f(x)')

# plot the figure in the second row and first column of the subplot figure
plt.subplot(212)
plt.grid()

# creating the plot representing y2 = cos(e^-2x) in the second row
plt.plot(x, np.cos(np.exp(-2*x)), 'b:')

# labeling the function being ploted 
plt.legend(['$y = cos(e^{-2x}$)'])
plt.ylabel('f(x)')
plt.xlabel('X')

# create title for super plot
plt.suptitle('Multiple Charts of f(x)')
plt.show()

