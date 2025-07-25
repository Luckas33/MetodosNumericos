def regra_um_terco_simpson(f, a, b):
    h = (b - a) / 2
    x1 = a + h
    return (h / 3) * (f(a) + 4 * f(x1) + f(b))
