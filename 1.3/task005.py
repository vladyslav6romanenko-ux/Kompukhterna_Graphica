import numpy as np
import utils
if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)
    R1 = utils.get_euler_matrix([30, 90, 45], 'XYZ')
    R2 = utils.get_euler_matrix([40, 90, 35], 'XYZ')
    cube1 = utils.apply_transformation(cube, R1)
    cube2 = utils.apply_transformation(cube, R2)
    print("Matrices equal:", np.allclose(R1, R2))
    scene = utils.create_scene("Task 5 Lost Axis Demo")
    utils.draw_3d_cube(scene, cube1, color='red')
    utils.draw_3d_cube(scene, cube2, color='blue')
    utils.render_scene(scene, "task005_lost_axis.png")
