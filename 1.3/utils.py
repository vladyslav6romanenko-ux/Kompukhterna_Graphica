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

def rotation_x_matrix(angle_deg):
    c = np.cos(np.radians(angle_deg))
    s = np.sin(np.radians(angle_deg))
    return np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, c, -s, 0.0],
        [0.0, s, c, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=float)

def rotation_y_matrix(angle_deg):
    c = np.cos(np.radians(angle_deg))
    s = np.sin(np.radians(angle_deg))
    return np.array([
        [c, 0.0, s, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-s, 0.0, c, 0.0],
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

def get_euler_matrix(angles, order='XYZ'):
    ax, ay, az = angles
    Rx = rotation_x_matrix(ax)
    Ry = rotation_y_matrix(ay)
    Rz = rotation_z_matrix(az)
    if order == 'XYZ':
        return Rz @ Ry @ Rx
    elif order == 'ZYX':
        return Rx @ Ry @ Rz
    return np.eye(4)

def apply_transformation(points, matrix):
    hom_points = np.hstack((points, np.ones((len(points), 1))))
    transformed = (matrix @ hom_points.T).T
    return transformed[:, :3]

def draw_3d_cube(scene, points, color='blue', alpha=1.0):
    faces = [
        [0, 1, 2, 3], [4, 5, 6, 7],
        [0, 1, 5, 4], [2, 3, 7, 6],
        [1, 2, 6, 5], [0, 3, 7, 4]
    ]
    for face in faces:
        face_pts = [tuple(float(c) for c in points[i][:3]) for i in face]
        scene.add_figure(SimplePolygon(*face_pts, color=color), name=str(uuid.uuid4()))

def create_scene(title="3D Scene"):
    return Scene(coordinate_rect=(-15, -15, -15, 15, 15, 15), title=title, axis_show=True)

def render_scene(scene, output_path=None):
    scene._prepare()
    scene._draw_frames()
    scene.figure.canvas.draw()
    if output_path is not None:
        scene.figure.savefig(output_path, bbox_inches="tight")
    scene.show()
