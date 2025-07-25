def regra_um_terco_simpson_repetida(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("O número de subintervalos 'n' deve ser par para a regra de 1/3 de Simpson.")
    
    h = (b - a) / n
    soma = f(a) + f(b)
    
    for i in range(1, n, 2):  # Termos ímpares (multiplicados por 4)
        soma += 4 * f(a + i * h)
        
    for i in range(2, n, 2):  # Termos pares (multiplicados por 2)
        soma += 2 * f(a + i * h)
        
    return (h / 3) * soma