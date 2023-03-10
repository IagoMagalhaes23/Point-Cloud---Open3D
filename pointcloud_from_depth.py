import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d


def compute_pcd_nested_loops(depth_im):
    height, width = depth_im.shape
    pcd = []
    for i in range(height):
        for j in range(width):
            z = depth_image[i][j]
            x = (j - CX_DEPTH) * depth_im[i][j] / FX_DEPTH
            y = (i - CY_DEPTH) * depth_im[i][j] / FY_DEPTH
            pcd.append([x, y, z])
    return pcd


def compute_pcd_vectorization(depth_im):
    height, width = depth_im.shape
    jj = np.tile(range(width), height)
    ii = np.repeat(range(height), width)
    z = depth_im.reshape(height * width)
    pcd = np.dstack([(ii - CX_DEPTH) * z / FX_DEPTH,
                    (jj - CY_DEPTH) * z / FY_DEPTH,
                    z]).reshape((length, 3))
    return pcd


if __name__ == '__main__':
    FX_DEPTH = 5.8262448167737955e+02
    FY_DEPTH = 5.8269103270988637e+02
    CX_DEPTH = 3.1304475870804731e+02
    CY_DEPTH = 2.3844389626620386e+02

    depth_image = iio.imread('data/depth.png')

    print(f"Image resolution: {depth_image.shape}")
    print(f"Data type: {depth_image.dtype}")
    print(f"Min value: {np.min(depth_image)}")
    print(f"Max value: {np.max(depth_image)}")

    depth_grayscale = np.array(256 * depth_image / 0x0fff, dtype=np.uint8)
    iio.imwrite('results/depth_grayscale.png', depth_grayscale)

    fig, axs = plt.subplots(1, 2)
    axs[0].imshow(depth_image, cmap="gray")
    axs[0].set_title('Depth image')
    axs[1].imshow(depth_grayscale, cmap="gray")
    axs[1].set_title('Depth grayscale image')
    plt.show()

    height, width = depth_image.shape

    jj = np.tile(range(width), height)
    ii = np.repeat(range(height), width)

    xx = (jj - CX_DEPTH) / FX_DEPTH
    yy = (ii - CY_DEPTH) / FY_DEPTH

    length = height * width
    z = depth_image.reshape(length)

    pcd = np.dstack((xx * z, yy * z, z)).reshape((length, 3))

    pcd_o3d = o3d.geometry.PointCloud()
    pcd_o3d.points = o3d.utility.Vector3dVector(pcd)

    o3d.visualization.draw_geometries([pcd_o3d])