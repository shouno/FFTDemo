#
# -*- coding: utf-8 -*-
#

import numpy as np
import matplotlib.pylab as plt

N = 512

x = np.linspace(0, 2*np.pi, N)
y = 8 * np.sin(x) + 5 * np.cos(2*x) + np.sin(6 * x)

plt.clf()
plt.plot(x, y, linewidth=2)
plt.title('y=8 sin(x) + 5 cos(2x) + sin(6x)')
plt.grid()
plt.xlim(0, 2 * np.pi)
plt.ylim(-15, 10)
plt.show()
plt.savefig('synth.png')

plt.clf()
plt.plot(x, 8 * np.sin(x), linewidth=2)
plt.title('8 sin(x)')
plt.grid()
plt.xlim(0, 2 * np.pi)
plt.ylim(-15, 10)
plt.show()
plt.savefig('8sin.png')

plt.clf()
plt.plot(x, 5 * np.cos(2*x), linewidth=2)
plt.title('5 cos(2x)')
plt.grid()
plt.xlim(0, 2 * np.pi)
plt.ylim(-15, 10)
plt.show()
plt.savefig('5cos2.png')

plt.clf()
plt.plot(x, np.sin(6*x), linewidth=2)
plt.title('sin(6x)')
plt.grid()
plt.xlim(0, 2 * np.pi)
plt.ylim(-15, 10)
plt.show()
plt.savefig('sin6.png')



