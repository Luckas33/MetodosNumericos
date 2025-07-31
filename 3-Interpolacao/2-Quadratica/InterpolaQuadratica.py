def InterpolaQuadratica(x0, y0, x1, y1, x2, y2, x):
    # Evita divisões por zero
    if x0 == x1 or x0 == x2 or x1 == x2:
        raise ValueError("Os valores de x devem ser distintos.")
    
    # Lagrange
    L0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    L1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    L2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))

    # Polinômio interpolador
    P = y0 * L0 + y1 * L1 + y2 * L2
    return P