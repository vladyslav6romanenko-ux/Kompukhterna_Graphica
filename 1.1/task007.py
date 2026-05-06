import numpy as np
import utils

if __name__ == '__main__':
    polygon = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    polygon_hom = utils.standard2homogeneous(polygon)

    pivots = np.array([[0.5, 0.5], [0, 1], [1, 1], [2, 2]])
    rotation = utils.get_rotation_matrix(60)

    for i, pivot in enumerate(pivots):
        matrix = utils.transformation_relative_to_pivot(rotation, pivot)
        res_hom = utils.apply_transformation_matrix(matrix, polygon_hom)
        res = utils.homogeneous2standard(res_hom)

        print(matrix)
        print(res)

        utils.draw_polygone_with_pivot(polygon, res, pivot, f"task007_image_{i+1}", (-2, -2, 4, 4))
