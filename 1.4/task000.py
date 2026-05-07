import numpy as np
import utils

if __name__ == '__main__':
    axis = np.array([1, 1, 1], dtype=float) / np.sqrt(3)
    angle = 60

    print("Підзавдання 1. Побудувати одиничний кватерніон q:")
    q = utils.quat_from_axis_angle(axis, angle)
    print(q)

    print("\nПідзавдання 2. Обчислити норму отриманого кватерніона:")
    norm = utils.quat_norm(q)
    print(norm)

    print("\nПідзавдання 3. Побудувати матрицю повороту R:")
    R = utils.quat_to_matrix(q)
    print(R)
