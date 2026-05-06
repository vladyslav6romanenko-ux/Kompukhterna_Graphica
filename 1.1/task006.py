import numpy as np
import utils

if __name__ == '__main__':
    polygon = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    polygon_hom = utils.standard2homogeneous(polygon)

    scale = utils.get_scale_matrix(1, 3)
    rotation = utils.get_rotation_matrix(60)
    translation = utils.get_translation_matrix(2, 3)

    M_order1 = translation @ rotation @ scale
    res1_hom = utils.apply_transformation_matrix(M_order1, polygon_hom)
    res1 = utils.homogeneous2standard(res1_hom)

    M_order2 = rotation @ scale @ translation
    res2_hom = utils.apply_transformation_matrix(M_order2, polygon_hom)
    res2 = utils.homogeneous2standard(res2_hom)

    step1 = utils.homogeneous2standard(utils.apply_transformation_matrix(scale, polygon_hom))
    step2 = utils.homogeneous2standard(utils.apply_transformation_matrix(rotation @ scale, polygon_hom))

    print(scale)
    print(step1)
    print(rotation)
    print(step2)
    print(translation)
    print(M_order1)
    print(res1)
    print(M_order2)
    print(res2)

    utils.draw_polygone_no_pivot(polygon, res1, "task006_order1", (-3, -1, 6, 8))
    utils.draw_polygone_no_pivot(polygon, res2, "task006_order2", (-3, -1, 6, 8))
