import numpy as np
import utils

if __name__ == '__main__':
    polygon = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    polygon_hom = utils.standard2homogeneous(polygon)

    scale = utils.get_scale_matrix(1, 3)
    rotation = utils.get_rotation_matrix(60)

    step1_hom = utils.apply_transformation_matrix(scale, polygon_hom)
    step1 = utils.homogeneous2standard(step1_hom)

    step2_matrix = rotation @ scale
    step2_hom = utils.apply_transformation_matrix(step2_matrix, polygon_hom)
    step2 = utils.homogeneous2standard(step2_hom)

    print(scale)
    print(step1)
    print(rotation)
    print(step2)
    print(step2_matrix)

    utils.draw_polygone_no_pivot(polygon, step2, "task004", (-3, -1, 4, 5))
