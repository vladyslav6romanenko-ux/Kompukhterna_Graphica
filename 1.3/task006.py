import numpy as np
import utils
if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)
    scene = utils.create_scene("Task 6 Interpolation")
    for t in np.linspace(0, 1, 5):
        angles = t * np.array([90, 90, 90])
        R = utils.get_euler_matrix(angles, 'XYZ')
        cube_t = utils.apply_transformation(cube, R)
        utils.draw_3d_cube(scene, cube_t, color='cyan')
    utils.render_scene(scene, "task006_interpolation.png")
