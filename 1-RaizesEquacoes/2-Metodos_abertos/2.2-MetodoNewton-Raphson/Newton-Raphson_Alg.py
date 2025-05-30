import math
import numpy as np

def iteracao (x, f,df):
    return x - (f(x))/(df(x))

def iteracoes(x_atual,x_ante,f,df,Tol,iter):
    x_ante = x_atual
    x_atual = iteracao(x_ante,f,df)
    erro = np.abs((x_atual - x_ante)/x_atual) 
    iter += 1
    
    return x_atual,x_ante,erro, iter

def newtonRaphsonNalg(x0,nalg,f,df,Tol,iterMax):
    if nalg  < 0 and iterMax < 0: return None
    
    iter = 1
    x_ante = x0
    x_atual = iteracao(x0,f,df)

    erro = ((x_atual - x0)/x_atual) 
    
    if(nalg == 0):
        while(erro > Tol and iter < iterMax):
            x_atual, x_ante,erro, iter = iteracoes(x_atual,x_ante,f,df, Tol ,iter)
    else:
        while(np.abs(x_atual - x_ante) > 10**(-nalg-1) and iter < iterMax):
            x_atual, x_ante,erro, iter = iteracoes(x_atual,x_ante,f,df, Tol ,iter)
    return x_atual,erro, iter


def fxl(x):
  return (-1)*np.sin(x) - 2*x

def f(x):
  return np.cos(x) - x**2

[xr , erro, niter]  = newtonRaphsonNalg(1, 8, f, fxl,1e-5,2000) # Essa aq é a q vale de verdade
print (xr, erro, niter)