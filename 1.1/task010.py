import numpy as np
import utils

if __name__ == '__main__':
    polygon = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    polygon_hom = utils.standard2homogeneous(polygon)

    pivot = np.array([0.5, 0.5])
    scale = utils.get_scale_matrix(2, 2)
    rotation = utils.get_rotation_matrix(30)
    translation = utils.get_translation_matrix(1, -1)

    scale_pivot = utils.transformation_relative_to_pivot(scale, pivot)
    rotation_pivot = utils.transformation_relative_to_pivot(rotation, pivot)

    M1 = translation @ rotation_pivot @ scale_pivot
    M2 = rotation_pivot @ scale_pivot @ translation
    M3 = rotation_pivot @ translation @ scale_pivot

    res1 = utils.homogeneous2standard(utils.apply_transformation_matrix(M1, polygon_hom))
    res2 = utils.homogeneous2standard(utils.apply_transformation_matrix(M2, polygon_hom))
    res3 = utils.homogeneous2standard(utils.apply_transformation_matrix(M3, polygon_hom))

    print(M1)
    print(M2)
    print(M3)
    print(res1)
    print(res2)
    print(res3)

    utils.draw_polygone_with_pivot(polygon, res1, pivot, "task010_image_1", (-2, -2, 5, 5))
    utils.draw_polygone_with_pivot(polygon, res2, pivot, "task010_image_2", (-2, -2, 5, 5))
    utils.draw_polygone_with_pivot(polygon, res3, pivot, "task010_image_3", (-2, -2, 5, 5))
