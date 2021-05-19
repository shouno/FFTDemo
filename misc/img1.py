# -*- coding: utf-8 -*-


import numpy as np
import scipy as sp
from scipy import misc
import matplotlib.pylab as plt


l = misc.lena()

plt.imshow( l )
plt.gray()



q = l[210:274, 210:274]

