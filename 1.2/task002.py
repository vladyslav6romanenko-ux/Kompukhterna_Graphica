import numpy as np
import utils

if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)

    S = utils.scale_matrix(2, 0.5, 1)
    Rx = utils.rotation_x_matrix(30)
    Ry = utils.rotation_y_matrix(45)
    Rz = utils.rotation_z_matrix(60)
    R_euler = Rz @ Ry @ Rx

    T = utils.translation_matrix(-3, 2, 5)

    M = T @ R_euler @ S
    cube_final = utils.apply_transformation(cube, M)

    scene = utils.create_scene("Task 2")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_final, color='green')
    utils.render_scene(scene, "task002.png")
