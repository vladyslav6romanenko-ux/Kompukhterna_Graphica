import numpy as np
import utils

if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)

    pivot = [1, 2, 3]
    S_base = utils.scale_matrix(3, 1, 1)
    S_pivot = utils.get_pivot_matrix(S_base, pivot)

    R_base = utils.rotation_z_matrix(30)
    R_pivot = utils.get_pivot_matrix(R_base, pivot)

    M = R_pivot @ S_pivot
    cube_final = utils.apply_transformation(cube, M)

    scene = utils.create_scene("Task 7")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_final, color='magenta')
    utils.render_scene(scene, "task007.png")
