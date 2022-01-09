from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.gridspec as gridspec
import matplotlib.colors as mcolors

def main():
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111, projection='3d')
    r = 1
    u=np.linspace(-2,2,200)
    v=np.linspace(0,2*np.pi,60)
    [u,v]=np.meshgrid(u,v)

    a = 1.25
    b = 1.25
    c = 6.5

    mycmap = truncate_colormap(plt.get_cmap("Greens"), 0.4, 2)
    plotting(ax,a,b,c,u,v,mycmap)

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=-1):
    if n == -1:
        n = cmap.N
    new_cmap = mcolors.LinearSegmentedColormap.from_list(
         'trunc({name},{a:.2f},{b:.2f})'.format(name=cmap.name, a=minval, b=maxval),
         cmap(np.linspace(minval, maxval, n)))
    return new_cmap

def plotting(ax,a,b,c,u,v,mycmap):
    x = a*np.cosh(u)*np.cos(v) +4.8
    y = b*np.cosh(u)*np.sin(v) +4.8
    z = c*np.sinh(u) + 22
    ax.plot_surface(x, y, z, alpha=1, rstride=4, cstride=4, cmap=mycmap.reversed())

    ax.set_xlabel('Hua Gu')
    ax.set_ylabel('Length/9.2cm')
    ax.set_zlabel('Height/47cm')
    ax.set_xlim(-1,10)
    ax.set_ylim(-1,10)
    ax.set_zlim(0,50)

    p = Circle((4.8, 4.8), 4.5, color='green', alpha=0.5)
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")
    plt.show()

if __name__ == '__main__':
    main()

