import numpy as np
import utils

def decompose_affine(M):
    T = M[:3, 3]
    R_S = M[:3, :3]
    sx = np.linalg.norm(R_S[:, 0])
    sy = np.linalg.norm(R_S[:, 1])
    sz = np.linalg.norm(R_S[:, 2])

    S = np.array([sx, sy, sz])
    R = R_S / S
    return T, S, R

if __name__ == '__main__':
    M = utils.translation_matrix(5, -2, 4) @ utils.rotation_z_matrix(45) @ utils.scale_matrix(2, 3, 1)

    T, S, R = decompose_affine(M)
    is_ortho = np.allclose(R @ R.T, np.eye(3))

    trace = np.trace(R)
    angle = np.degrees(np.arccos((trace - 1) / 2))

    print("Translation:", T)
    print("Scale:", S)
    print("Rotation Matrix:\n", R)
    print("Is Orthogonal?", is_ortho)
    print(f"Rotation Angle: {angle:.2f} deg")
