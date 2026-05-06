import numpy as np
import utils

if __name__ == '__main__':
    polygon = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    polygon_hom = utils.standard2homogeneous(polygon)

    translation = utils.get_translation_matrix(1, -1)
    scale = utils.get_scale_matrix(2, 2)

    step1_hom = utils.apply_transformation_matrix(translation, polygon_hom)
    step1 = utils.homogeneous2standard(step1_hom)

    step2_matrix = scale @ translation
    step2_hom = utils.apply_transformation_matrix(step2_matrix, polygon_hom)
    step2 = utils.homogeneous2standard(step2_hom)

    print(translation)
    print(step1)
    print(scale)
    print(step2)
    print(step2_matrix)

    utils.draw_polygone_no_pivot(polygon, step2, "task005", (-1, -3, 5, 5))
