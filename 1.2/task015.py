import numpy as np
import utils

if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)

    S_pivot = utils.get_pivot_matrix(utils.scale_matrix(2, 2, 2), [1, 1, 1])
    R_int = utils.rotation_x_matrix(90)
    T_ext = utils.translation_matrix(-3, 4, 2)

    M = T_ext @ S_pivot @ R_int
    cube_final = utils.apply_transformation(cube, M)

    scene = utils.create_scene("Task 15")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_final, color='darkred')
    utils.render_scene(scene, "task015.png")
