import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'


xLim = 2*np.pi
yLim = 2*np.pi
xValues = np.linspace(-xLim, xLim, 1000)
yValues = np.linspace(-yLim, yLim, 1000)
X, Y = np.meshgrid(xValues, yValues)
f = .5

wave1 = np.sin(2*np.pi*f*np.sqrt((X - xLim/3)**2 + (Y - yLim/2)**2))
wave2 = np.sin(2*np.pi*f*np.sqrt((X + xLim/3)**2 + (Y + yLim/2)**2))
z = wave1 + wave2

fig, ax = plt.subplots()
ax.contourf(X, Y, z, 100, cmap='RdBu')
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_xticks([])
ax.set_yticks([])
plt.savefig('Interferenzen.png', dpi=1000, bbox_inches='tight')
plt.show()