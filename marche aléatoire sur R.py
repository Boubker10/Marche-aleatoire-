import numpy as np
import matplotlib.pyplot as plt
n = 5000
x = np.cumsum(np.random.randn(n))
y = np.cumsum(np.random.randn(n))
k = 10
x2 = np.interp(np.arange(n * k), np.arange(n) * k, x)
y2 = np.interp(np.arange(n * k), np.arange(n) * k, y)
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax.scatter(x2, y2, c=range(n * k), linewidths=0.5, 
           marker='o', s=1,cmap=plt.cm.jet,)
ax.axis('equal')
plt.title('Marche aléatoire dans le plan (x,y)')
plt.grid()
plt.xlabel('position en x')
plt.ylabel('position en y')
plt.show()
