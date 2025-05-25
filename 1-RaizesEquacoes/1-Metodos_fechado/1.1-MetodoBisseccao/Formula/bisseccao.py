import math
import matplotlib as lib
import numpy as np

def fx(x):
  return np.sqrt(x)-np.cos(x)

def bisseccao(a,b,tolerancia,maximo):
    x_anterior = a
    x_atual = (b+a)/2
    count_atual = 1

    fxa = fx(a)
    fxb = fx(b)
    fx_atual = fx(x_atual)

    print(x_atual)
    erro = np.abs((x_atual - a) / x_atual)


    if fx_atual * fxa < 0:
        b = x_atual
    else: 
        if fx_atual * fxb < 0:
            a = x_atual
        else:
            if x_atual == 0:
                return x_atual, erro
            else:
                print ("erro")
                return None
    
    while erro > tolerancia and count_atual < maximo:
        x_anterior = x_atual
        fxa = fx(a)
        fxb = fx(b)
        x_atual = (b + a ) / 2
        print(x_atual)

        fx_atual = fx(x_atual)
        erro = np.abs((x_atual - x_anterior) / x_atual)

        if fx_atual*fxa < 0:
            b = x_atual
        else:
            a = x_atual
        count_atual += 1
    return x_atual,erro
        
    
[Sol, erro] = bisseccao(0,1,0.001, 20)


print(Sol)
print(erro)