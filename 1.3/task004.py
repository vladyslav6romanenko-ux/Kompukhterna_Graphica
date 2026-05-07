import sympy as sp
import numpy as np
import utils
if __name__ == '__main__':
    a, b, g = sp.symbols('alpha beta gamma')
    Rx = sp.Matrix([[1, 0, 0], [0, sp.cos(a), -sp.sin(a)], [0, sp.sin(a), sp.cos(a)]])
    Ry = sp.Matrix([[sp.cos(b), 0, sp.sin(b)], [0, 1, 0], [-sp.sin(b), 0, sp.cos(b)]])
    Rz = sp.Matrix([[sp.cos(g), -sp.sin(g), 0], [sp.sin(g), sp.cos(g), 0], [0, 0, 1]])
    R = Rz * Ry * Rx
    R_lock = R.subs(b, sp.pi/2)
    print(sp.simplify(R_lock))
    cube = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1]], dtype=float)
    R_val = utils.get_euler_matrix([0, 90, 0], 'XYZ')
    cube_locked = utils.apply_transformation(cube, R_val)
    scene = utils.create_scene("Task 4 Gimbal Lock State")
    utils.draw_3d_cube(scene, cube_locked, color='orange')
    utils.render_scene(scene, "task004_gimbal.png")
