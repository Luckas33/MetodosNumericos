def InterpolaLinear(x0, y0, x1, y1, x):
    if x1 == x0:
        raise ValueError("Divisão por zero: x0 e x1 não podem ser iguais.")
    
    y = y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)
    return y