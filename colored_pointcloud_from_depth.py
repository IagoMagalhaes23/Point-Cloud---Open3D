import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d


def compute_colored_pointcloud_nested_loops(depth_image, rgb_image):

    height, width = depth_image.shape
    colors = []
    pcd = []
    for i in range(height):
        for j in range(width):
            z = depth_image[i][j]
            x = (j - CX_DEPTH) * z / FX_DEPTH
            y = (i - CY_DEPTH) * z / FY_DEPTH

            [x_RGB, y_RGB, z_RGB] = np.linalg.inv(R).dot([x, y, z]) - np.linalg.inv(R).dot(T)

            j_rgb = int((x_RGB * FX_RGB) / z_RGB + CX_RGB + width / 2)
            i_rgb = int((y_RGB * FY_RGB) / z_RGB + CY_RGB)

            pcd.append([x, y, z])

            if 0 <= j_rgb < width and 0 <= i_rgb < height:
                colors.append(rgb_image[i_rgb][j_rgb])
            else:
                colors.append([0., 0., 0.])
    return [np.array(pcd), np.array(colors)]


if __name__ == '__main__':
    FX_DEPTH = 5.8262448167737955e+02
    FY_DEPTH = 5.8269103270988637e+02
    CX_DEPTH = 3.1304475870804731e+02
    CY_DEPTH = 2.3844389626620386e+02

    FX_RGB = 5.1885790117450188e+02
    FY_RGB = 5.1946961112127485e+02
    CX_RGB = 3.2558244941119034e+0
    CY_RGB = 2.5373616633400465e+02

    R = -np.array([[9.9997798940829263e-01, 5.0518419386157446e-03, 4.3011152014118693e-03],
                   [-5.0359919480810989e-03, 9.9998051861143999e-01, -3.6879781309514218e-03],
                   [- 4.3196624923060242e-03, 3.6662365748484798e-03, 9.9998394948385538e-01]])

    T = np.array([2.5031875059141302e-02, -2.9342312935846411e-04, 6.6238747008330102e-04])

    depth_image = iio.imread('data/depth.png')
    rgb_image = iio.imread('data/rgb.jpg')

    fig, axs = plt.subplots(1, 2)
    axs[0].imshow(depth_image, cmap="gray")
    axs[0].set_title('Depth image')
    axs[1].imshow(rgb_image)
    axs[1].set_title('RGB image')
    plt.show()

    height, width = depth_image.shape

    jj = np.tile(range(width), height)
    ii = np.repeat(range(height), width)

    xx = (jj - CX_DEPTH) / FX_DEPTH
    yy = (ii - CY_DEPTH) / FY_DEPTH

    length = height * width
    z = depth_image.reshape(length)

    pcd = np.dstack((xx * z, yy * z, z)).reshape((length, 3))
    cam_RGB = np.apply_along_axis(np.linalg.inv(R).dot, 1, pcd) - np.linalg.inv(R).dot(T)
    xx_rgb = ((cam_RGB[:, 0] * FX_RGB) / cam_RGB[:, 2] + CX_RGB + width / 2).astype(int).clip(0, width - 1)
    yy_rgb = ((cam_RGB[:, 1] * FY_RGB) / cam_RGB[:, 2] + CY_RGB).astype(int).clip(0, height - 1)
    colors = rgb_image[yy_rgb, xx_rgb]

    pcd_o3d = o3d.geometry.PointCloud()
    pcd_o3d.points = o3d.utility.Vector3dVector(pcd)
    pcd_o3d.colors = o3d.utility.Vector3dVector(np.array(colors / 255))
    
    o3d.visualization.draw_geometries([pcd_o3d])