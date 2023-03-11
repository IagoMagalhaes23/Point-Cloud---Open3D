import numpy as np
import open3d as o3d
from sklearn.cluster import KMeans, DBSCAN
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    pcd = o3d.io.read_point_cloud("data/depth_2_pcd_downsampled.ply")
    points = np.asarray(pcd.points)

    scaled_points = StandardScaler().fit_transform(points)

    #model = DBSCAN(eps=0.15, min_samples=10)
    model = KMeans(n_clusters=4)
    model.fit(scaled_points)

    labels = model.labels_
    n_clusters = len(set(labels))

    colors = plt.get_cmap("tab20")(labels / (n_clusters if n_clusters > 0 else 1))
    colors[labels < 0] = 0
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])

    o3d.visualization.draw_geometries([pcd])