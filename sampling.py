'''
    Autor: Iago Magalhães
'''

import open3d as o3d

mesh = o3d.io.read_triangle_mesh("data/bunny.ply")

mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh])

pcd = mesh.sample_points_uniformly(number_of_points=1000)

o3d.visualization.draw_geometries([pcd])

o3d.io.write_point_cloud("results/bunny_pcd.ply", pcd)
