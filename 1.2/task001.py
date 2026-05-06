import numpy as np
import utils

if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)

    R = utils.rotation_axis_matrix(45, [1, 1, 0])
    T = utils.translation_matrix(2, -1, 3)

    cube_step1 = utils.apply_transformation(cube, R)
    cube_step2 = utils.apply_transformation(cube_step1, T)

    print("Matrix R:\n", R)
    print("Matrix T:\n", T)

    scene = utils.create_scene("Task 1")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_step2, color='red')
    utils.render_scene(scene, "task001.png")
