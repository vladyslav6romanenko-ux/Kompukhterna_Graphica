import numpy as np
import utils

if __name__ == '__main__':
    tet = np.array([[0,0,0], [1,0,0], [0,1,0], [0,0,1]], dtype=float)

    q1 = utils.quat_from_axis_angle([1, 0, 0], 45)
    q2 = utils.quat_from_axis_angle([0, 1, 0], 30)

    print("Підзавдання 3. Обчислити результуючий кватерніон q_total = q2 * q1:")
    q_total = utils.quat_multiply(q2, q1)
    print(q_total)

    print("\nПідзавдання 4. Визначити параметри (вісь та кут):")
    axis, angle = utils.quat_to_axis_angle(q_total)
    print("Вісь:", axis)
    print("Кут:", angle)

    print("\nПідзавдання 5. Обчислити нові координати вершин тетраедра:")
    tet_rotated = utils.apply_quat_transformation(tet, q_total)
    print(tet_rotated)

    scene = utils.create_scene("Task 2 Quaternion Rot")
    utils.draw_3d_tetrahedron(scene, tet, color='gray')
    utils.draw_3d_tetrahedron(scene, tet_rotated, color='blue')
    utils.render_scene(scene, "task002.png")
