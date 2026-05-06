import numpy as np
import utils

if __name__ == '__main__':
    tet = np.array([[0,0,0], [1,0,0], [0,1,0], [0,0,1]], dtype=float)

    angle = np.random.uniform(10, 90)
    axis = np.random.uniform(-1, 1, 3)
    tx, ty, tz = np.random.uniform(-5, 5, 3)

    R = utils.rotation_axis_matrix(angle, axis)
    T = utils.translation_matrix(tx, ty, tz)

    M = T @ R
    tet_final = utils.apply_transformation(tet, M)

    scene = utils.create_scene("Task 5")
    utils.draw_3d_tetrahedron(scene, tet, color='gray')
    utils.draw_3d_tetrahedron(scene, tet_final, color='purple')
    utils.render_scene(scene, "task005.png")
