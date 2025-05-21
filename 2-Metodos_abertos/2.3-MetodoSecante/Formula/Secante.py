import math
import numpy as np


def iteracao(f, x0, x1):
    return ((x0*f(x1) - x1*f(x0))/(f(x1) - f(x0)))

def Secante(x0, x1, f ,Tol, maxIter):
    
    iter = 1
    x_atual = iteracao(f,x0,x1)
    
    erro = np.abs((x_atual - x0)/x_atual) * 100
    
    while (erro > Tol and iter < maxIter):
        x_anterior = x_atual
        x_atual = iteracao(f,x_anterior, x_atual)
        
        erro = np.abs((x_atual - x_anterior)/x_atual) * 100
        iter += 1
        
    return x_atual, erro, iter
