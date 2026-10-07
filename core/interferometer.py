import numpy as np

def multi_reflection_path(points, passes=2):
    """Return a schematic ray path through a multi-mirror Michelson layout."""
    if passes < 1:
        raise ValueError("passes must be >= 1")
    points = np.asarray(points, dtype=float)
    path = [points[0]]
    for _ in range(passes):
        path.extend(points[1:])
        path.extend(points[-2:0:-1])
    return np.asarray(path)

def rotated_arms(theta_deg, arm=2.7):
    th = np.deg2rad(theta_deg)
    a = np.array([arm*np.cos(th), arm*np.sin(th)])
    b = np.array([arm*np.cos(th+np.pi/2), arm*np.sin(th+np.pi/2)])
    return a, b

def ray_segments(theta_deg=0, extended=False):
    a, b = rotated_arms(theta_deg)
    if not extended:
        return [np.array([-2.2,0.0]), np.array([0.0,0.0]), a, np.array([0.0,0.0]), b, np.array([0.0,0.0])]
    # Historical-inspired schematic with auxiliary folding mirrors.
    m1 = a
    m2 = a * 0.62
    m3 = b
    m4 = b * 0.62
    return [np.array([-2.2,0.0]), np.array([0.0,0.0]), m2, m1, m2, np.array([0.0,0.0]), m4, m3, m4, np.array([0.0,0.0])]
