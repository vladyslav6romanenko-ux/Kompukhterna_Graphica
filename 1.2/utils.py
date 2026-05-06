import sys
import os
import uuid
from pathlib import Path

os.environ.setdefault("GRAPHIC_ENGINE_MPL_BACKEND", "Agg")

ENGINE_ROOT = Path(__file__).resolve().parent
if str(ENGINE_ROOT) not in sys.path:
    sys.path.append(str(ENGINE_ROOT))

if (ENGINE_ROOT.parent / "GraphicEngine2D").exists():
    if str(ENGINE_ROOT.parent / "GraphicEngine2D") not in sys.path:
        sys.path.append(str(ENGINE_ROOT.parent / "GraphicEngine2D"))

import numpy as np
from src.engine.scene.Scene import Scene
from src.engine.model.SimplePolygon import SimplePolygon

# --- 3D MATH ---

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

def rotation_axis_matrix(angle_deg, axis):
    axis = np.array(axis, dtype=float)
    axis /= np.linalg.norm(axis)
    ux, uy, uz = axis
    c = np.cos(np.radians(angle_deg))
    s = np.sin(np.radians(angle_deg))
    one_c = 1.0 - c

    return np.array([
        [c + ux**2 * one_c, ux*uy*one_c - uz*s, ux*uz*one_c + uy*s, 0.0],
        [uy*ux*one_c + uz*s, c + uy**2 * one_c, uy*uz*one_c - ux*s, 0.0],
        [uz*ux*one_c - uy*s, uz*uy*one_c + ux*s, c + uz**2 * one_c, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=float)

def get_pivot_matrix(matrix, pivot):
    px, py, pz = pivot
    T_to = translation_matrix(-px, -py, -pz)
    T_back = translation_matrix(px, py, pz)
    return T_back @ matrix @ T_to

def apply_transformation(points, matrix):
    hom_points = np.hstack((points, np.ones((len(points), 1))))
    transformed = (matrix @ hom_points.T).T
    return transformed[:, :3]

# --- VISUALIZATION ---

def draw_3d_cube(scene, points, color='blue'):
    faces = [
        [0, 1, 2, 3], [4, 5, 6, 7],
        [0, 1, 5, 4], [2, 3, 7, 6],
        [1, 2, 6, 5], [0, 3, 7, 4]
    ]
    for face in faces:
        # Передаємо кортежі з 3 елементів (x, y, z), щоб пройти валідацію в BaseModel
        face_pts = [tuple(float(c) for c in points[i][:3]) for i in face]
        scene.add_figure(SimplePolygon(*face_pts, color=color), name=str(uuid.uuid4()))

def draw_3d_tetrahedron(scene, points, color='blue'):
    faces = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
    for face in faces:
        face_pts = [tuple(float(c) for c in points[i][:3]) for i in face]
        scene.add_figure(SimplePolygon(*face_pts, color=color), name=str(uuid.uuid4()))

def draw_3d_surface(scene, points, color='blue'):
    pts = [tuple(float(c) for c in pt[:3]) for pt in points]
    scene.add_figure(SimplePolygon(*pts, color=color), name=str(uuid.uuid4()))

def create_scene(title="3D Scene"):
    # Для 3D рушія потрібні 6 координат: (min_x, min_y, min_z, max_x, max_y, max_z)
    return Scene(coordinate_rect=(-10, -10, -10, 15, 15, 15), title=title, axis_show=True)

def render_scene(scene, output_path=None):
    scene._prepare()
    scene._draw_frames()
    scene.figure.canvas.draw()
    if output_path is not None:
        scene.figure.savefig(output_path, bbox_inches="tight")
    # Щоб не було TypeError (show() takes 1 argument)
    scene.show()
