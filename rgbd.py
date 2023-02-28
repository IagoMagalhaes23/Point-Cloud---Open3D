'''
    Autor: Iago Magalhães
'''

import open3d as o3d

rgb_image = o3d.io.read_image("data/rgb.jpg")
depth_image = o3d.io.read_image("data/depth.png")

rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(rgb_image, depth_image, convert_rgb_to_intensity=False)

pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image,o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))

o3d.visualization.draw_geometries([pcd])
