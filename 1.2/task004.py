import numpy as np
import utils

if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)

    Rz = utils.rotation_z_matrix(20)
    Ry = utils.rotation_y_matrix(35)
    Rx = utils.rotation_x_matrix(50)
    R_euler = Rx @ Ry @ Rz

    T = utils.translation_matrix(1, 3, -2)

    M = T @ R_euler
    cube_final = utils.apply_transformation(cube, M)

    scene = utils.create_scene("Task 4")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_final, color='orange')
    utils.render_scene(scene, "task004.png")
