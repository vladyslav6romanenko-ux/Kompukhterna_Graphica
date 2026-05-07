import numpy as np
import utils
if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)
    R = utils.get_euler_matrix([20, 35, 50], 'ZYX')
    T = utils.translation_matrix(1, 3, -2)
    M = T @ R
    cube_final = utils.apply_transformation(cube, M)
    scene = utils.create_scene("Task 2")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_final, color='blue')
    utils.render_scene(scene, "task002.png")
