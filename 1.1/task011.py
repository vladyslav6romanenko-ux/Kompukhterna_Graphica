import numpy as np
import utils

if __name__ == '__main__':
    T = np.array([
        [2.934, -0.416, 2.000],
        [0.624,  1.956, 3.400],
        [0.0,    0.0,   1.0]
    ])

    polygon = np.array([[2, 3.4], [4.9, 4], [4.5, 6], [1.6, 5.4]])
    polygon_hom = utils.standard2homogeneous(polygon)

    inv_T = np.linalg.inv(T)
    print(inv_T)

    polygon_local_hom = utils.apply_transformation_matrix(inv_T, polygon_hom)
    polygon_local = utils.homogeneous2standard(polygon_local_hom)

    print(polygon_local)

    utils.draw_polygone_no_pivot(polygon_local, polygon, "task011_image", (-1, -1, 7, 7))
