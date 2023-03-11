import open3d as o3d
import numpy as np

if __name__ == '__main__':
    pcd = o3d.io.read_point_cloud("data/depth_2_pcd.ply")

    points = np.asarray(pcd.points)
    pass_through_filter = np.logical_and(points[:, 2] >= 0.8, points[:, 2] <= 2.5)
    filtered_points = points[pass_through_filter]

    filtered_pcd = o3d.geometry.PointCloud()
    filtered_pcd.points = o3d.utility.Vector3dVector(filtered_points)

    colors = np.asarray(pcd.colors)
    filtered_pcd.colors = o3d.utility.Vector3dVector(colors[pass_through_filter])

    o3d.visualization.draw_geometries([filtered_pcd])

    colors[pass_through_filter] = [0., 1., 0.]
    pcd.colors = o3d.utility.Vector3dVector(colors)
    o3d.visualization.draw_geometries([pcd])
