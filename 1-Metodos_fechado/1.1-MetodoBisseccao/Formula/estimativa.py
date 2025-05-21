import math
import matplotlib as lib
import numpy as np
import bisseccao


def estimativa(a,b,tolerancia,max):
    return ((np.log(b-a) - np.log(tolerancia))/np.log(2))