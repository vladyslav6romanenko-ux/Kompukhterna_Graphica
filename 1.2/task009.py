import numpy as np
import utils

if __name__ == '__main__':
    rect = np.array([[1,2,0], [4,2,0], [4,5,0], [1,5,0]], dtype=float)
    pivot = [3, 3, 0]

    Ry_base = utils.rotation_y_matrix(60)
    Ry_pivot = utils.get_pivot_matrix(Ry_base, pivot)

    Rx_base = utils.rotation_x_matrix(30)
    Rx_pivot = utils.get_pivot_matrix(Rx_base, pivot)

    M = Rx_pivot @ Ry_pivot
    rect_final = utils.apply_transformation(rect, M)

    scene = utils.create_scene("Task 9")
    utils.draw_3d_surface(scene, rect, color='gray')
    utils.draw_3d_surface(scene, rect_final, color='teal')
    utils.render_scene(scene, "task009.png")
