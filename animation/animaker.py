from animation import make_animation
import numpy as np
from numpy import pi, e

#make
t = np.arange(1e-10, (pi/2) - 1e-10, 0.01)
xlim = [-1, 1]
ylim = [-1, 1]
val = [0, 10]

f1 = [lambda i: np.cos(t) ** i,
     lambda i: np.sin(t) ** i, "b"]
     
f2 = [lambda i: - np.cos(t) ** i, 
      lambda i: np.sin(t) ** i, "b"]
      
f3 = [lambda i: np.cos(t) ** i,
      lambda i: - np.sin(t) ** i, "b"]
     
f4 = [lambda i: - np.cos(t) ** i,
      lambda i: - np.sin(t) ** i, "b"]

name = "circle.gif"

make_animation(name, (f1, f2, f3, f4), val, xlim=xlim, ylim=ylim)
