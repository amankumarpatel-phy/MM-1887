import math
import numpy as np

C = 299_792_458.0

def round_trip_times(L, v):
    beta = v / C
    if not 0 <= beta < 1:
        raise ValueError("Require 0 <= v < c.")
    t_parallel = 2 * L * C / (C**2 - v**2)
    t_perpendicular = 2 * L / (C * math.sqrt(1 - beta**2))
    return t_parallel, t_perpendicular

def fringe_shift(L, wavelength, v):
    return 2 * L * (v / C) ** 2 / wavelength

def rotational_signal(L, wavelength, v, theta_deg):
    nmax = fringe_shift(L, wavelength, v)
    return 0.5 * nmax * np.cos(2 * np.deg2rad(theta_deg))

def phase_from_path_difference(path_difference, wavelength):
    return 2 * np.pi * path_difference / wavelength
