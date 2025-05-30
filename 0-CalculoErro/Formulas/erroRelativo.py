import math
import numpy as np


def erroRelativo(real,estimado):
    return np.abs((real - estimado)/real)