import numpy as np
import utils
def euler_from_matrix(R):
    beta = np.arcsin(-R[2, 0])
    if np.abs(np.cos(beta)) > 1e-6:
        alpha = np.arctan2(R[2, 1], R[2, 2])
        gamma = np.arctan2(R[1, 0], R[0, 0])
    else:
        alpha = 0.0
        gamma = np.arctan2(R[0, 1], R[0, 2])
    return np.degrees([alpha, beta, gamma])
if __name__ == '__main__':
    R_orig = utils.get_euler_matrix([10, 90, 20], 'XYZ')
    angles = euler_from_matrix(R_orig)
    R_recon = utils.get_euler_matrix(angles, 'XYZ')
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)
    c_orig = utils.apply_transformation(cube, R_orig)
    c_recon = utils.apply_transformation(cube, R_recon)
    scene = utils.create_scene("Task 7 Decomposition Check")
    utils.draw_3d_cube(scene, c_orig, color='gray')
    utils.draw_3d_cube(scene, c_recon, color='yellow')
    utils.render_scene(scene, "task007_decomp.png")
