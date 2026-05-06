import numpy as np
import utils

if __name__ == '__main__':
    polygon = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    polygon_hom = utils.standard2homogeneous(polygon)

    pivot = np.array([1, 1])
    scale = utils.get_scale_matrix(2, 1)
    translation = utils.get_translation_matrix(3, -2)

    scale_pivot = utils.transformation_relative_to_pivot(scale, pivot)

    M_order1 = translation @ scale_pivot
    M_order2 = scale_pivot @ translation

    res1 = utils.homogeneous2standard(utils.apply_transformation_matrix(M_order1, polygon_hom))
    res2 = utils.homogeneous2standard(utils.apply_transformation_matrix(M_order2, polygon_hom))

    print(res1)
    print(res2)

    utils.draw_polygone_with_pivot(polygon, res1, pivot, "task009_image_1", (-2, -3, 6, 4))
    utils.draw_polygone_with_pivot(polygon, res2, pivot, "task009_image_2", (-2, -3, 6, 4))
