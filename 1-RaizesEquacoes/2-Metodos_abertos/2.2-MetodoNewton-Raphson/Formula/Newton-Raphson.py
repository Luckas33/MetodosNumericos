import math
import numpy as np

def iteracao(f,df, x):
    return x - (f(x)/(df(x)))

def Newton_Raphson(x0, f, df ,Tol, maxIter):
    iter = 1
    
    x_atual = iteracao(f, df, x0)
    
    erro = np.abs((x_atual - x0) / x_atual) * 100
    
    while (erro > Tol and iter < maxIter):
        x_anterior = x_atual
        x_atual = iteracao(f, df, x_anterior)
        
        erro = np.abs((x_atual - x_anterior) / x_atual) * 100
        iter += 1
    
    return x_atual, erro, iter
