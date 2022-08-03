import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()
ax.set_aspect("equal")
ax.grid()
#ax.axis("off")
ax.set_xlim(-1.5, 1.5)

x = np.arange(-1.5, 1.5, 0.01)
y1 =  np.sqrt(np.abs(x)) - np.sqrt(1 - x**2)
y2 = np.sqrt(np.abs(x)) + np.sqrt(1 - x**2)

#ax.plot(x, y1, "r")
#ax.plot(x, y2, "r")
ax.fill_between(x, y1, y2, facecolor="red", alpha=0.8)

txt_xy = (-0.8, -0.8)
ax.text(*txt_xy, r"$ x^2 + (y - \sqrt{|x|} )^2 = 1$", horizontalalignment='center', fontsize=25)


plt.show()

#plt.savefig("heart.png")
