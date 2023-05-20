'''


160-Generate computer art

pip3 install numpy
pip3 install matplotlib

Developed by Abdul Rahman Al-Harbi

'''

import numpy as np
import matplotlib.pyplot as plt


N = 100
x = np.zeros(N)
y = np.zeros(N)

for i in range(N):
    x[i] = np.random.rand()
    y[i] = np.random.rand()
colors = np.random.rand(N)

area = (30 * np.random.rand(N))**3
ax = plt.subplot(111)
ax.scatter(x, y, s=area, c=colors, alpha=0.7)

ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

print("Developed by Abdul Rahman Al-Harbi")

plt.axis('off')
plt.show()
