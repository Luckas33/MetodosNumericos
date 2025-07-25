def regra_tres_oitavos_simpson_repetida(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("O número de subintervalos 'n' deve ser um múltiplo de 3 para a regra de 3/8 de Simpson.")
        
    h = (b - a) / n
    soma = f(a) + f(b)
    
    for i in range(1, n):
        if i % 3 == 0:
            soma += 2 * f(a + i * h)  # Múltiplos de 3
        else:
            soma += 3 * f(a + i * h)  # Outros termos
            
    return (3 * h / 8) * soma
