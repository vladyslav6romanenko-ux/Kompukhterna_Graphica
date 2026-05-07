import numpy as np
import utils

if __name__ == '__main__':
    p = np.array([1, 0, 0], dtype=float)
    axis = np.array([0, 0, 1], dtype=float)
    q = utils.quat_from_axis_angle(axis, 90)

    print("Підзавдання 1. Записати точку p у вигляді 'чистого' кватерніона v:")
    v = np.array([0, p[0], p[1], p[2]], dtype=float)
    print(v)

    print("\nПідзавдання 2. Виконати поворот точки v' = q * v * q^-1:")
    v_prime = utils.quat_multiply(utils.quat_multiply(q, v), utils.quat_inverse(q))
    print(v_prime)

    print("\nПідзавдання 3. Виділити векторну частину та перевірити з матричною трансформацією:")
    p_quat_rotated = v_prime[1:]
    R = utils.rotation_z_matrix(90)[:3, :3]
    p_mat_rotated = R @ p

    print("Векторна частина:", p_quat_rotated)
    print("Матрична трансформація:", p_mat_rotated)
    print("Збігаються?", np.allclose(p_quat_rotated, p_mat_rotated))
