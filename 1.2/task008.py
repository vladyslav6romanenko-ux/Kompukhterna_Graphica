import numpy as np
import utils

if __name__ == '__main__':
    tri = np.array([[1,2,3], [4,5,6], [7,8,9]], dtype=float)

    pivot = [2, 3, 4]
    axis = [1, 1, 1]

    R_base = utils.rotation_axis_matrix(90, axis)
    R_pivot = utils.get_pivot_matrix(R_base, pivot)

    T = utils.translation_matrix(0, -3, 2)

    M = T @ R_pivot
    tri_final = utils.apply_transformation(tri, M)

    scene = utils.create_scene("Task 8")
    utils.draw_3d_surface(scene, tri, color='gray')
    utils.draw_3d_surface(scene, tri_final, color='blue')
    utils.render_scene(scene, "task008.png")
