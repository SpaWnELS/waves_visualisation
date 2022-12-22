import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

plt.rcParams['text.usetex'] = True


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))

        return np.min(zs)


xValues = np.arange(0, 10 * np.pi, 0.1)
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

# Plot both arrows
a1 = Arrow3D([xValues[-2], xValues[-1]], [yValues[-2], yValues[-1]], [0, 0], mutation_scale=10, lw=1, arrowstyle="-|>", color='r')
a2 = Arrow3D([xValues[-2], xValues[-1]], [0, 0], [zValues[-2], zValues[-1]], mutation_scale=10, lw=1, arrowstyle="-|>", color='b')
ax.add_artist(a1)
ax.add_artist(a2)

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
plt.legend(prop={'size': 13})

plt.tight_layout()
plt.savefig('plot.png', dpi=1000)
plt.show()