#what is bar:
# A bar plot shows catergorical data as rectangular bars with
# the height of bars proportional to the value they represent. I
# t is often used to compare between
# values of different categories in the data

#how to create bar():
# With Pyplot, you can use the bar() function to draw bar graphs:
# Example
# Draw 4 bars:
import matplotlib.pyplot as plt
import numpy as np
# x =["A", "B", "C", "D"])
# y =[3, 8, 1, 10])
# plt.bar(x,y)
# plt.show()

# x = ["APPLES", "BANANAS"]
# y = [400, 350]
# plt.bar(x, y)
# plt.show()

#horizontal bar():
# Horizontal Bars
# If you want the bars to be displayed horizontally instead of vertically, use the barh() function:
# Example
# Draw 4 horizontal bars:
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.barh(x, y)
# plt.show()

#bar color
# Bar Color
# The bar() and barh() takes the keyword argument color to set the color of the bars:
# Example
# Draw 4 red bars:
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.bar(x, y, color = "yellow")
# plt.show()

# Color Hex
# Or you can use Hexadecimal color values:
# Example
# Draw 4 bars with a  green color:

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.bar(x, y, color = "#4CAF50")
# plt.show()

# Bar Width
# The bar() takes the keyword argument width to set the width of the bars:
# Example
# Draw 4 very thin bars:

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x, y, width = 0.3)
# plt.show()

# Bar Height
# The barh() takes the keyword argument height to set the height of the bars:
# Example
# Draw 4 very thin bars:

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.barh(x, y, height  = 0.1)
# plt.show()