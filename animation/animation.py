import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import pi
from PIL import Image


#円のアニメーション

def make_animation(saveName, funcs, valuable=[-1,1], xlim=[-1,1], ylim=[-1,1], frame=50):
    """save gif animation of function_graph
    saveName          : str
    funcs             : list  <-  [ ( x(i), y(i), color:str ), ...]  <-  x(i) / y(i) : (0 -> i -> 49)
    variable          : list  <-  [begin, end]
    xlim              : list
    ylim              : list
    -----------------------------------------------------
    return            : None
    """

    ims = []
    
    start = valuable[0]
    v_range = valuable[1] - valuable[0]
    
    for i in range(frame):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.set_aspect('equal')
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        #ax.axis("off")
        ax.grid("on")

        # 描画
        value = start + i*v_range/50
        for x, y, color in funcs:
            ax.plot(x(value), y(value), color)
            plt.close(fig)


        # 画像を保存
        fig.canvas.draw()
        im = np.array(fig.canvas.renderer.buffer_rgba())
        img = Image.fromarray(im)

        # 画像を追加
        ims.append(img)

        # figを削除
        del fig, ax

    ims[0].save(saveName, save_all=True, append_images=ims[1:])



"""
# function
xlim = ylim = [-2, 2]
v = [0, 2*pi]
t = np.arange(0, 2*pi, 0.01)
x1 = lambda i: (1- np.sin(i) + 1e-3 ) * np.cos(t)
y1 = lambda i: (1- np.cos(i) + 1e-3 ) * np.sin(t)
x2 = lambda i: np.cos(t) + np.cos(i**2)
y2 = lambda i: np.sin(t) + np.sin(i**2)
make_animation("anime1.gif",([x1, y1, "b"], [x2, y2, "g"]) ,v ,xlim=xlim, ylim=ylim)
"""

