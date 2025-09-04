import numpy as np


def rot_x(x: float, y: float, z: float, theta: float) -> np.ndarray:

    p = np.array([x, y, z])
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])
    return R @ p

def rot_y(x: float, y: float, z: float, theta: float) -> np.ndarray:

    p = np.array([x, y, z])
    R = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [ 0,            1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return R @ p

def rot_z(x: float, y: float, z: float, theta: float) -> np.ndarray:

    p = np.array([x, y, z])
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])
    return R @ p

def rotar(x: float, y: float, z: float, theta: float, axis: str) -> np.ndarray:
 
    if axis == 'x':
        return rot_x(x, y, z, theta)
    elif axis == 'y':
        return rot_y(x, y, z, theta)
    elif axis == 'z':
        return rot_z(x, y, z, theta)
    else:
        return None
