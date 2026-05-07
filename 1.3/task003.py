import numpy as np
import utils
if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)
    R_xyz = utils.get_euler_matrix([45, 30, 60], 'XYZ')
    R_zyx = utils.get_euler_matrix([45, 30, 60], 'ZYX')
    cube_xyz = utils.apply_transformation(cube, R_xyz)
    cube_zyx = utils.apply_transformation(cube, R_zyx)
    scene = utils.create_scene("Task 3 XYZ (Green) vs ZYX (Purple)")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_xyz, color='green')
    utils.draw_3d_cube(scene, cube_zyx, color='purple')
    utils.render_scene(scene, "task003_comparison.png")
