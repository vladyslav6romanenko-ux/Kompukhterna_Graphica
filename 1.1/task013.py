import numpy as np
import utils

if __name__ == '__main__':
    T = np.array([
        [1.414, -2.121, 1.0],
        [1.414,  2.121, 1.0],
        [0.0,    0.0,   1.0]
    ])

    polygon = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    polygon_hom = utils.standard2homogeneous(polygon)

    translation, rotation, scale = utils.decompose_TRS(T)
    utils.print_matrices([scale, rotation, translation], names=["Scale", "Rotation", "Translation"])

    polygon_transformed_hom = utils.apply_transformation_matrix(T, polygon_hom)
    polygon_transformed = utils.homogeneous2standard(polygon_transformed_hom)

    utils.draw_polygone_no_pivot(polygon, polygon_transformed, "task013_image", (-3, -3, 4, 5))
