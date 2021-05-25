import numpy as np
import matplotlib.pyplot as plt

xline = np.linspace(0, 15, 1000)
yline = np.sin(xline)
zline = np.cos(xline)


fig = plt.figure('3D Line', figsize=(9, 6))
ax = plt.axes(projection = '3d')

ax.plot3D(xline, yline, zline)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
