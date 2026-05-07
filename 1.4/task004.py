import numpy as np
import utils

if __name__ == '__main__':
    R = np.array([
        [0, -1, 0, 0],
        [1,  0, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ], dtype=float)

    print("Підзавдання 1. Знайти компоненти кватерніона, що відповідає матриці R:")
    q = utils.mat_to_quat(R)
    print(q)
