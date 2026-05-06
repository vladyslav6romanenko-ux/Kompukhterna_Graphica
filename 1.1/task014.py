import numpy as np
import utils

if __name__ == '__main__':
    T = np.array([
        [1.732, -1.0,   5.0],
        [1.0,    1.732, -3.0],
        [0.0,    0.0,   1.0]
    ])

    pivot = np.array([1.0, 1.0])

    M = T[:2, :2]
    sx = np.linalg.norm(M[:, 0])
    sy = np.linalg.norm(M[:, 1])
    scale = utils.get_scale_matrix(sx, sy)

    cos_theta = M[0, 0] / sx
    sin_theta = M[1, 0] / sx
    rotation = np.array([
        [cos_theta, -sin_theta, 0.0],
        [sin_theta,  cos_theta, 0.0],
        [0.0,        0.0,       1.0]
    ])

    RS_pivot = utils.transformation_relative_to_pivot(rotation @ scale, pivot)
    translation = T @ np.linalg.inv(RS_pivot)

    utils.print_matrices([scale, rotation, translation], names=["Scale", "Rotation", "Translation"])

    T_restored = translation @ RS_pivot
    print(np.allclose(T, T_restored))

    polygon = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    polygon_hom = utils.standard2homogeneous(polygon)

    polygon_transformed_hom = utils.apply_transformation_matrix(T, polygon_hom)
    polygon_transformed = utils.homogeneous2standard(polygon_transformed_hom)

    utils.draw_polygone_with_pivot(polygon, polygon_transformed, pivot, "task014_image", (-2, -4, 6, 4))
