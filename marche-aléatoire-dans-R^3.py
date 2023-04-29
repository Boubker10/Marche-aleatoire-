import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 5000
x = np.cumsum(np.random.randn(n))
y = np.cumsum(np.random.randn(n))
z = np.cumsum(np.random.randn(n))

# Création d'une liste de couleurs
colors = np.linspace(0, 1, n)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=colors, cmap=plt.cm.jet, linewidths=0.5, s=2)
ax.set_title('Marche aléatoire en 3D avec un gradient de couleur')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
