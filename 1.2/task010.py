import numpy as np
import utils

if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)
    pivot = [1, 1, 1]

    S_pivot = utils.get_pivot_matrix(utils.scale_matrix(2, 1, 1), pivot)
    Ry_pivot = utils.get_pivot_matrix(utils.rotation_y_matrix(45), pivot)
    T = utils.translation_matrix(-3, 4, 2)

    M = T @ Ry_pivot @ S_pivot
    cube_final = utils.apply_transformation(cube, M)

    scene = utils.create_scene("Task 10")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_final, color='red')
    utils.render_scene(scene, "task010.png")
