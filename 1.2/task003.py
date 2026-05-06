import numpy as np
import utils

if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)

    R1 = utils.rotation_z_matrix(60)
    R2 = utils.rotation_axis_matrix(45, [1, 1, 1])
    T = utils.translation_matrix(4, -2, 1)

    M = T @ R2 @ R1
    cube_final = utils.apply_transformation(cube, M)

    scene = utils.create_scene("Task 3")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_final, color='blue')
    utils.render_scene(scene, "task003.png")
