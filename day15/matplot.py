# What is Matplotlib?
# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
# Matplotlib was created by John D. Hunter.
# Matplotlib is open source and we can use it freely.
# Matplotlib is mostly written in python, a few segments are written in
# C, Objective-C and Javascript for Platform compatibility.
#import matplotlib
#plot
# Plotting x and y points
# The plot() function is used to draw points (markers) in a diagram.
# By default, the plot() function draws a line from point to point.
# The function takes parameters for specifying points in the diagram.
# Parameter 1 is an array containing the points on the x-axis.
# Parameter 2 is an array containing the points on the y-axis.
# If we need to plot a line from (1, 3) to (8, 10), we have
# to pass two arrays [1, 8] and [3, 10] to the plot function.

# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
# plt.plot(xpoints, ypoints)
# plt.show()

#matplotlib markers
# You can use the keyword argument marker to emphasize each point with a specified marker:
# Example
# Mark each point with a circle:
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()


