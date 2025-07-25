def regra_trapezio(f, a, b):
    h = b - a
    return (h / 2) * (f(a) + f(b))