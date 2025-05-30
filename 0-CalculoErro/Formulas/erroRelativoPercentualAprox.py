import math
import numpy as np

def erroRelativoAprox(x_atual,x_anterior):
    return np.abs((x_atual/x_anterior)) * 100