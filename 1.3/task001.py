import numpy as np
import utils
if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)
    S = utils.scale_matrix(2, 0.5, 1)
    R = utils.get_euler_matrix([30, 45, 60], 'XYZ')
    T = utils.translation_matrix(-3, 2, 5)
    M = T @ R @ S
    cube_final = utils.apply_transformation(cube, M)
    scene = utils.create_scene("Task 1")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_final, color='red')
    utils.render_scene(scene, "task001.png")
