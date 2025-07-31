def diferenDividida(x, y):
    n = len(x)
    coef = y.copy()
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef

def interpolaNewton(x, coef, X):
    n = len(coef) - 1
    p = coef[n]
    for k in range(n-1, -1, -1):
        p = p * (X - x[k]) + coef[k]
    return p