import numpy as np
import utils

if __name__ == '__main__':
    T = np.array([
        [0.866, 0.5,   4.0],
        [0.5,   0.866, 3.0],
        [0.0,   0.0,   1.0]
    ])

    print(T)

    try:
        utils.decompose_TRS(T)
    except ValueError as e:
        print(e)

    polygon = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    polygon_hom = utils.standard2homogeneous(polygon)

    polygon_transformed_hom = utils.apply_transformation_matrix(T, polygon_hom)
    polygon_transformed = utils.homogeneous2standard(polygon_transformed_hom)

    utils.draw_polygone_no_pivot(polygon, polygon_transformed, "task012_image", (-1, -1, 6, 6))
