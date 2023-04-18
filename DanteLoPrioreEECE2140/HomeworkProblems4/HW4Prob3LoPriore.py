import numpy as np
import matplotlib.pyplot as plt

# Dante LoPriore
# March 28, 2023
# PS4: Problem 3

# Purpose: to create a plot of two functions in range of -4pi <= x <= 4pi, where
# x = cos(t) + 2*cos(t/4) and y = sin(t) - 2*sin(t/4)

# initialize t limits
t_min = -4*(np.pi)
t_max = 4*(np.pi)
t = np.arange(t_min, t_max, 0.25)

plt.figure()

# creating the plot representing x = cos(t) + 2*cos(t/4) and y = sin(t) - 2*sin(t/4)
plt.plot((np.cos(t) + (2*(np.cos(t/4)))), (np.sin(t) - (2*(np.sin(t/4)))), 'b-', marker='*')

# labeling the function being ploted 
plt.grid()
plt.ylabel('y = sin(t) - 2*sin(t/4)')
plt.xlabel('x = cos(t) + 2*cos(t/4)')
plt.title("Y vs. X", loc='center')
plt.show()


