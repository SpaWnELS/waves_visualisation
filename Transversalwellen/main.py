import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams['text.usetex'] = True

xValues = np.arange(0, 10*np.pi, 0.1)
yValues = np.sin(xValues)
zValues = np.sin(xValues)

points1 = [(x, y, 0) for x, y in zip(xValues, yValues)]
points2 = [(x, 0, z) for x, z in zip(xValues, zValues)]

# Create figure
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot both curves
ax.plot(xValues, yValues, np.zeros(len(xValues)), 'r', linewidth=1, label=r'$y=\sin(x)$')
ax.plot(xValues, np.zeros(len(xValues)), zValues, 'b', linewidth=1, label=r'$z=\sin(x)$')

# Fill the area under the two curves
ax.add_collection3d(Poly3DCollection([points1], facecolors='r', alpha=.1))
ax.add_collection3d(Poly3DCollection([points2], facecolors='b', alpha=.1))

ax.grid(False)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
ax.set_xlabel(r'x')
ax.set_ylabel(r'y')
ax.set_zlabel(r'z')
plt.legend()

plt.tight_layout()
plt.savefig('plot.png', dpi=1000)