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

Z = np.sin( X )
