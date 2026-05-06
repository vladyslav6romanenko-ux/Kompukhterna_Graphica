import numpy as np
import utils

if __name__ == '__main__':
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)

    Rx = utils.rotation_x_matrix(30)
    Ry = utils.rotation_y_matrix(45)
    Rz = utils.rotation_z_matrix(60)

    R_ext = Rz @ Ry @ Rx

    Rx_int = utils.rotation_x_matrix(60)
    Ry_int = utils.rotation_y_matrix(45)
    Rz_int = utils.rotation_z_matrix(30)

    R_int = Rz_int @ Ry_int @ Rx_int

    cube_ext = utils.apply_transformation(cube, R_ext)
    cube_int = utils.apply_transformation(cube, R_int)

    print("Extrinsic:\n", R_ext)
    print("Intrinsic:\n", R_int)
    print("Ідентичні?", np.allclose(R_ext, R_int))

    scene = utils.create_scene("Task 11 Extrinsic")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_ext, color='red')
    utils.render_scene(scene, "task011_extrinsic.png")
