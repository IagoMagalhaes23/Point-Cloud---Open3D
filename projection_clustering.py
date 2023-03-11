import numpy as np
import open3d as o3d
from sklearn.cluster import KMeans, DBSCAN, OPTICS
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    pcd = o3d.io.read_point_cloud("data/depth_2_pcd_downsampled.ply")
    o3d.visualization.draw_geometries([pcd])
    points = np.asarray(pcd.points).copy()

    points[:, 1] = 0
    pcd_projected = o3d.geometry.PointCloud()
    pcd_projected.points = o3d.utility.Vector3dVector(points)
    o3d.visualization.draw_geometries([pcd_projected])

    points_xz = points[:, [0, 2]]
    scaled_points = StandardScaler().fit_transform(points_xz)
    model = DBSCAN(eps=0.15, min_samples=10)
    model.fit(scaled_points)

    labels = model.labels_
    n_clusters = len(set(labels))

    colors = plt.get_cmap("tab20")(labels / (n_clusters if n_clusters > 0 else 1))
    colors[labels < 0] = 0
    pcd_projected.colors = o3d.utility.Vector3dVector(colors[:, :3])
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

    o3d.visualization.draw_geometries([pcd_projected])
    o3d.visualization.draw_geometries([pcd])