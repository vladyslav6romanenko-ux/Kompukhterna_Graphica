import numpy as np
import utils

if __name__ == '__main__':
    M = np.array([
        [0, -2, 0,   10],
        [1,  0, 0,  -5],
        [0,  0, 1.5, 3],
        [0,  0, 0,   1]
    ], dtype=float)

    print("Підзавдання 1. Вилучення трансляції T:")
    T = M[:3, 3]
    print(T)

    print("\nПідзавдання 2. Вилучення масштабування S:")
    RS = M[:3, :3]
    sx = np.linalg.norm(RS[:, 0])
    sy = np.linalg.norm(RS[:, 1])
    sz = np.linalg.norm(RS[:, 2])
    S = np.array([sx, sy, sz])
    print(S)

    print("\nПідзавдання 3. Отримання чистої матриці обертання R:")
    R = RS / S
    print(R)
    print("Ортогональна?", np.allclose(R.T @ R, np.eye(3)))

    print("\nПідзавдання 4. Конвертація в кватерніон q:")
    M_rot = np.eye(4)
    M_rot[:3, :3] = R
    q = utils.mat_to_quat(M_rot)
    print(q)

    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)
    cube_final = utils.apply_transformation(cube, M)

    scene = utils.create_scene("Task 5 Full Decomp")
    utils.draw_3d_cube(scene, cube, color='gray')
    utils.draw_3d_cube(scene, cube_final, color='red')
    utils.render_scene(scene, "task005.png")
