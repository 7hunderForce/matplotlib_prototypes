import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-15, 15, 100)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

fig = plt.figure('3D Contour', figsize=(9, 6))
ax = plt.axes(projection = '3d')

contour_weight = 100 # 0 to 100
ax.contour3D(X, Y, Z, contour_weight, cmap = 'viridis')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
