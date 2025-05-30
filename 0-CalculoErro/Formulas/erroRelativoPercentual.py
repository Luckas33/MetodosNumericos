import math
import numpy as np


def erroRelativoPerc(absoluto,verdadeiro):
    return (absoluto/np.abs(verdadeiro)) * 100