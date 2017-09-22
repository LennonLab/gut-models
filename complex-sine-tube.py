import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from numpy import pi

freq, amp = 1, 1
x, y = np.mgrid[-5*pi:5*pi:300j, -5*pi:5*pi:300j]
data = ((amp)*np.sin((x*freq)))*((amp)*np.sin((y*freq)))
h, w = data.shape

theta, z = np.linspace(0, 2 * np.pi, w), np.linspace(0, 1, h)
THETA, Z = np.meshgrid(theta, z)

X = np.cos(THETA)
Y = np.sin(THETA)

for i in range(300):
    for j in range(300):

        if X[i,j] < 0:
            X[i,j] += 0.2 * data[i,j]
        elif X[i,j] > 0:
            X[i,j] -= 0.2 * data[i,j]

        if Y[i,j] < 0:
            Y[i,j] += 0.2 * data[i,j]
        elif Y[i,j] > 0:
            Y[i,j] -= 0.2 * data[i,j]


fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

cmap = plt.get_cmap('jet')
plot = ax.plot_surface(
    X, Y, np.sin(Z), rstride=1, cstride=1, facecolors=cmap(data),
    linewidth=0, antialiased=False, alpha=1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
