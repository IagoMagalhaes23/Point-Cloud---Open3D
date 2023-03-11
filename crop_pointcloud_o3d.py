import numpy as np
import open3d as o3d
import math
import itertools

if __name__ == '__main__':
    pcd = o3d.io.read_point_cloud("data/depth_2_pcd.ply")

    bounds = [[-math.inf, math.inf], [-math.inf, math.inf], [0.8, 2]]
    bounding_box_points = list(itertools.product(*bounds))
    bounding_box = o3d.geometry.AxisAlignedBoundingBox.create_from_points(
        o3d.utility.Vector3dVector(bounding_box_points))

    pcd_croped = pcd.crop(bounding_box)

    o3d.visualization.draw_geometries([pcd_croped])