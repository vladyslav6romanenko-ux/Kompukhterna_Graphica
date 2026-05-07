import sys
import os
import uuid
from pathlib import Path
import numpy as np

os.environ.setdefault("GRAPHIC_ENGINE_MPL_BACKEND", "Agg")

ENGINE_ROOT = Path(__file__).resolve().parent
if str(ENGINE_ROOT) not in sys.path:
    sys.path.append(str(ENGINE_ROOT))

if (ENGINE_ROOT.parent / "GraphicEngine2D").exists():
    if str(ENGINE_ROOT.parent / "GraphicEngine2D") not in sys.path:
        sys.path.append(str(ENGINE_ROOT.parent / "GraphicEngine2D"))

from src.engine.scene.Scene import Scene
from src.engine.model.SimplePolygon import SimplePolygon

def translation_matrix(x, y, z):
    return np.array([
        [1.0, 0.0, 0.0, x],
        [0.0, 1.0, 0.0, y],
        [0.0, 0.0, 1.0, z],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=float)

def scale_matrix(sx, sy, sz):
    return np.array([
        [sx, 0.0, 0.0, 0.0],
        [0.0, sy, 0.0, 0.0],
        [0.0, 0.0, sz, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=float)

def rotation_z_matrix(angle_deg):
    c = np.cos(np.radians(angle_deg))
    s = np.sin(np.radians(angle_deg))
    return np.array([
        [c, -s, 0.0, 0.0],
        [s, c, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=float)

def quat_multiply(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2
    ], dtype=float)

def quat_conjugate(q):
    w, x, y, z = q
    return np.array([w, -x, -y, -z], dtype=float)

def quat_norm(q):
    return np.linalg.norm(q)

def quat_inverse(q):
    return quat_conjugate(q) / (quat_norm(q)**2)

def quat_from_axis_angle(axis, angle_deg):
    axis = np.array(axis, dtype=float)
    axis /= np.linalg.norm(axis)
    half_angle = np.radians(angle_deg) / 2
    s = np.sin(half_angle)
    return np.array([np.cos(half_angle), axis[0]*s, axis[1]*s, axis[2]*s], dtype=float)

def quat_to_axis_angle(q):
    w, x, y, z = q
    angle = 2 * np.arccos(w)
    s = np.sqrt(1 - w*w)
    if s < 1e-8:
        axis = np.array([1, 0, 0], dtype=float)
    else:
        axis = np.array([x, y, z], dtype=float) / s
    return axis, np.degrees(angle)

def quat_to_matrix(q):
    w, x, y, z = q
    return np.array([
        [1 - 2*y*y - 2*z*z, 2*x*y - 2*z*w,     2*x*z + 2*y*w,     0],
        [2*x*y + 2*z*w,     1 - 2*x*x - 2*z*z, 2*y*z - 2*x*w,     0],
        [2*x*z - 2*y*w,     2*y*z + 2*x*w,     1 - 2*x*x - 2*y*y, 0],
        [0,                 0,                 0,                 1]
    ], dtype=float)

def mat_to_quat(M):
    R = M[:3, :3]
    trace = np.trace(R)
    if trace > 0:
        S = np.sqrt(trace + 1.0) * 2
        w = 0.25 * S
        x = (R[2, 1] - R[1, 2]) / S
        y = (R[0, 2] - R[2, 0]) / S
        z = (R[1, 0] - R[0, 1]) / S
    elif (R[0, 0] > R[1, 1]) and (R[0, 0] > R[2, 2]):
        S = np.sqrt(1.0 + R[0, 0] - R[1, 1] - R[2, 2]) * 2
        w = (R[2, 1] - R[1, 2]) / S
        x = 0.25 * S
        y = (R[0, 1] + R[1, 0]) / S
        z = (R[0, 2] + R[2, 0]) / S
    elif R[1, 1] > R[2, 2]:
        S = np.sqrt(1.0 + R[1, 1] - R[0, 0] - R[2, 2]) * 2
        w = (R[0, 2] - R[2, 0]) / S
        x = (R[0, 1] + R[1, 0]) / S
        y = 0.25 * S
        z = (R[1, 2] + R[2, 1]) / S
    else:
        S = np.sqrt(1.0 + R[2, 2] - R[0, 0] - R[1, 1]) * 2
        w = (R[1, 0] - R[0, 1]) / S
        x = (R[0, 2] + R[2, 0]) / S
        y = (R[1, 2] + R[2, 1]) / S
        z = 0.25 * S
    q = np.array([w, x, y, z], dtype=float)
    return q / np.linalg.norm(q)

def apply_quat_to_point(q, p):
    v = np.array([0, p[0], p[1], p[2]], dtype=float)
    q_inv = quat_inverse(q)
    v_prime = quat_multiply(quat_multiply(q, v), q_inv)
    return v_prime[1:]

def apply_transformation(points, matrix):
    hom_points = np.hstack((points, np.ones((len(points), 1))))
    transformed = (matrix @ hom_points.T).T
    return transformed[:, :3]

def apply_quat_transformation(points, q):
    return np.array([apply_quat_to_point(q, p) for p in points])

def draw_3d_cube(scene, points, color='blue'):
    faces = [
        [0, 1, 2, 3], [4, 5, 6, 7],
        [0, 1, 5, 4], [2, 3, 7, 6],
        [1, 2, 6, 5], [0, 3, 7, 4]
    ]
    for face in faces:
        face_pts = [tuple(float(c) for c in points[i][:3]) for i in face]
        scene.add_figure(SimplePolygon(*face_pts, color=color), name=str(uuid.uuid4()))

def draw_3d_tetrahedron(scene, points, color='blue'):
    faces = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
    for face in faces:
        face_pts = [tuple(float(c) for c in points[i][:3]) for i in face]
        scene.add_figure(SimplePolygon(*face_pts, color=color), name=str(uuid.uuid4()))

def create_scene(title="3D Scene"):
    return Scene(coordinate_rect=(-10, -10, -10, 15, 15, 15), title=title, axis_show=True)

def render_scene(scene, output_path=None):
    scene._prepare()
    scene._draw_frames()
    scene.figure.canvas.draw()
    if output_path is not None:
        scene.figure.savefig(output_path, bbox_inches="tight")
    scene.show()
