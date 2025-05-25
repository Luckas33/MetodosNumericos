import math
import numpy as np

def RetaSecante(a,b,f):
    return (a*f(b)-b*f(a))/(f(b)-f(a))
    

def FalsaPosicao(a, b, f, Tol, maxIter):
    if f(a) * f(b) >= 0:
        print("Não há raiz no intervalo [a, b]")
        return None

    iter = 0
    x_anterior = a
    x_atual = RetaSecante(a, b, f)
    erro = np.abs((x_atual - x_anterior) / x_atual) * 100

    while erro > Tol and iter < maxIter:
        fx_atual = f(x_atual)

        if f(a) * fx_atual < 0:
            b = x_atual
        else:
            a = x_atual

        x_anterior = x_atual
        x_atual = RetaSecante(a, b, f)
        erro = np.abs((x_atual - x_anterior) / x_atual) * 100
        iter += 1

    return x_atual, erro, iter
    