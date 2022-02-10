# matplotlib is a python package used for 2d graphics.
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
x=[5,7,8]
y=[12,16,6]

x2=[6,9,11]
y2=[12,16,6]
plt.plot(x,y,"g",label="lineone", linewidth=5)
plt.plot(x2,y2,"c",label="linetwo", linewidth=5)
plt.legend()
plt.grid(True,color="k")
plt.show()