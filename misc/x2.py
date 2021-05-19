# -*- coding: utf-8 -*-
#

import numpy as np
import scipy as sp
import matplotlib.pylab as plt

N = 128
x = range( N ) / np.double(N) * 2 - 1
y = x**2

plt.plot( x, y )

Y = np.fft.fft( y )

cutoff = 3
flt = np.zeros(N)
flt[:cutoff] = 1
flt[-cutoff+1:] = 1

Ydash = Y * flt

ydash = np.fft.ifft( Ydash )

