import numpy as np
from vector import Vector
from typing import Union, Tuple
""" 

The electric field intensity E at an arbitrary point P(x, y, z)

due to a line charge with uniform charge density rho
extending from A(0, 0, z1) to B(0, 0, z2)

"""
eps0 = 8.854 * 1.0e-12  # free space permittivity
T = Union[int, float]


def ElecFieldOfLineCharge(rho: T, A: Vector, B: Vector,
                          P: Vector) -> Tuple[Vector, float, Vector]:
    r = np.sqrt(P.x * P.x + P.y * P.y)
    alpha1 = np.arctan2(np.abs(P.z - A.z), r)
    alpha2 = np.arctan2(np.abs(P.z - B.z), r)

    factor = rho / (4.0 * np.pi * eps0 * r)

    Efield = factor * Vector(-(np.sin(alpha2) - np.sin(alpha1)), 0.0,
                             np.cos(alpha2) - np.cos(alpha1))
    intensity = Efield.norm()
    uniVec = Efield / intensity

    return Efield, intensity, uniVec
