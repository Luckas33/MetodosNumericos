def regra_tres_oitavos_simpson(f, a, b):
    h = (b - a) / 3
    x1 = a + h
    x2 = a + 2 * h
    return (3 * h / 8) * (f(a) + 3 * f(x1) + 3 * f(x2) + f(b))