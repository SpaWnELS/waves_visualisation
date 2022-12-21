import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.rcParams['text.usetex'] = True

xValues = np.arange(0, 10, 0.1)
sinValues = np.sin(xValues)

timeSteps1 = np.arange(0, 10, 1)
timeSteps2 = np.arange(0, 10, .5)
timeSteps3 = np.arange(0, 10, .1)
# Create figure
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

ax1.plot(xValues, sinValues, 'b', linewidth=1.5)
ax1.plot(timeSteps1, np.sin(timeSteps1), '--r', linewidth=1.5)
ax1.scatter(timeSteps1, np.sin(timeSteps1), c='r', s=25)

ax2.plot(xValues, sinValues, 'b', linewidth=1.5)
ax2.plot(timeSteps2, np.sin(timeSteps2), '--r', linewidth=1.5)
ax2.scatter(timeSteps2, np.sin(timeSteps2), c='r', s=25)

ax3.plot(xValues, sinValues, 'b', linewidth=1.5)
ax3.plot(timeSteps3, np.sin(timeSteps3), '--r', linewidth=1.5)
ax3.scatter(timeSteps3, np.sin(timeSteps3), c='r', s=25)

ax1.set_ylabel(r'$u(x, t)$', fontsize=13)
ax2.set_yticklabels([])
ax3.set_yticklabels([])

for ax in [ax1, ax2, ax3]:
    ax.grid(False)
    ax.set_xlabel(r'$x$', fontsize=13)

ax1.set(title=r'Maschenweite $h=1$')
ax2.set(title=r'Maschenweite $h=0.5$')
ax3.set(title=r'Maschenweite $h=0.1$')

plt.savefig('Zeitschritte.png', dpi=1000, bbox_inches='tight')
