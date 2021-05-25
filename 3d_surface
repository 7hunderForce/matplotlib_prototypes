import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-15, 15, 100)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

fig = plt.figure(figsize=(9, 6))
ax = plt.axes(projection = '3d')

ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'inferno')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(60, 95)

plt.show()
