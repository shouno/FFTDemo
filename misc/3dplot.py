# -*- coding: utf-8 -*-
#

import numpy as np
import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

N = 256
x = ( range( N ) / np.double(N) * 2 ) * np.pi
y = ( range( N ) / np.double(N) * 2 ) * np.pi

X, Y = np.meshgrid( x, y )
Z = np.sin(X)

fig = plt.figure()
ax = fig.gca( projection='3d' )

surf = ax.plot_surface( X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim( -1.1, 1.1 )

fig.colorbar( surf, shrink=0.5, aspect=5 )
plt.show()

#imshow( Z, cmap=cm.coolwarm )



