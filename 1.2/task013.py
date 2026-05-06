import numpy as np
import utils

if __name__ == '__main__':
    tet = np.array([[0,0,0], [1,0,0], [0,1,0], [0,0,1]], dtype=float)

    R1 = utils.rotation_x_matrix(45)
    T = utils.translation_matrix(2, 0, 0)
    R2 = utils.rotation_y_matrix(30)

    M = R1 @ T @ R2
    tet_final = utils.apply_transformation(tet, M)

    scene = utils.create_scene("Task 13")
    utils.draw_3d_tetrahedron(scene, tet, color='gray')
    utils.draw_3d_tetrahedron(scene, tet_final, color='navy')
    utils.render_scene(scene, "task013.png")
