def lagrange(x_pontos, y_pontos, x):
    if len(x_pontos) != len(y_pontos):
        raise ValueError("Listas de x e y devem ter o mesmo tamanho.")

    n = len(x_pontos)
    P = 0

    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_pontos[j]) / (x_pontos[i] - x_pontos[j])
        P += y_pontos[i] * L_i

    return P