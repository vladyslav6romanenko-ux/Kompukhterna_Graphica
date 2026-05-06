import numpy as np
import utils

if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)

    pivot = [2, 0, 3]
    R_base = utils.rotation_y_matrix(45)
    R_pivot = utils.get_pivot_matrix(R_base, pivot)

    T = utils.translation_matrix(-1, 2, 4)

    M = T @ R_pivot
    cube_final = utils.apply_transformation(cube, M)

    scene = utils.create_scene("Task 6")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_final, color='cyan')
    utils.render_scene(scene, "task006.png")
