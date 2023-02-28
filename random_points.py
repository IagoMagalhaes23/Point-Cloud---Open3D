'''
    Autor: Iago Magalhães
'''

import numpy as np
import matplotlib.pyplot as plt

number_points = 50
pcd = np.random.rand(number_points, 3)
print(pcd)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter3D(pcd[:, 0], pcd[:, 1], pcd[:, 2])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Random Point Cloud")
plt.show()
