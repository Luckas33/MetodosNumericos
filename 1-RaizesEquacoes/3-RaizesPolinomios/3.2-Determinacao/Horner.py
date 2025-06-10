def horner(z, a):
    n = len(a) - 1
    b = a[n]
    for j in range(n - 1, -1, -1):
        b = a[j] + b * z
    return b

# Coeficientes do polinômio (exemplo: x⁴ - 3x³ + 7x² + 3x + 3)
a = [1, -3, 7, 3, 3]

# Avaliar o polinômio em z = 2
print(horner(2, a))
