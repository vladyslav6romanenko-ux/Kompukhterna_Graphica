import numpy as np
import utils

if __name__ == '__main__':
    polygon = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    polygon_hom = utils.standard2homogeneous(polygon)

    pivots = np.array([[0.5, 0.5], [0, 1], [1, 1], [2, 2]])
    scale = utils.get_scale_matrix(2, 3)

    for i, pivot in enumerate(pivots):
        matrix = utils.transformation_relative_to_pivot(scale, pivot)
        res_hom = utils.apply_transformation_matrix(matrix, polygon_hom)
        res = utils.homogeneous2standard(res_hom)

        print(matrix)
        print(res)

        utils.draw_polygone_with_pivot(polygon, res, pivot, f"task008_image_{i+1}", (-3, -3, 6, 6))
