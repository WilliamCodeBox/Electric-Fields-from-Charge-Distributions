""" Infinite sheet of charge in the xy-plane with uniform charge density """
from vector import Vector
import numpy as np
from typing import Tuple, Union

eps0 = 8.854 * 1.0e-12  # free space permittivity
T = Union[int, float]


def InfiniteSheetCharge(rho: T) -> Tuple[Vector, float, Vector]:
    sign = rho / np.abs(rho)
    intensity = np.abs(rho) / (2.0 * eps0)
    uniVec = Vector(0, 0, sign)

    Efield = intensity * uniVec

    return Efield, intensity, uniVec


def ElecFieldOfParallelPlateCapacitor(rho: T) -> Tuple[Vector, float, Vector]:
    sign = rho / np.abs(rho)
    intensity = np.abs(rho) / eps0
    uniVec = Vector(0, 0, sign)
    Efield = intensity * uniVec
    return Efield, intensity, uniVec


if __name__ == "__main__":
    pass