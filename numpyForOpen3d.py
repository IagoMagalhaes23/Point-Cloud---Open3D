'''
    Autor: Iago Magalhães
'''

import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d

number_points = 2000
pcd_np = np.random.rand(number_points, 3)

pcd_o3d = o3d.geometry.PointCloud()
pcd_o3d.points = o3d.utility.Vector3dVector(pcd_np)

o3d.visualization.draw_geometries([pcd_o3d])

pcd_o3d = o3d.io.read_point_cloud("data/bunny_pcd.ply")

pcd_np = np.asarray(pcd_o3d.points)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter3D(pcd_np[:, 0], pcd_np[:, 2], pcd_np[:, 1])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Bunny Point Cloud")

plt.show()
