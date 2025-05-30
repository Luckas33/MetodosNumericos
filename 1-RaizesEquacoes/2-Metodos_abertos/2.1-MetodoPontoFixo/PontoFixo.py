import numpy as np

def g(x):
    return 3/x 

def PontoFixo (g,x0,tol,maxIter) :
    it = 1
    
    #Primeira iteração
    x_atual = g(x0)
    erro = np.abs(x_atual-x0/x_atual) * 100
    
    #Segunda iteração
    while(erro > tol and it < maxIter):
        x_ant = x_atual
        erro = np.abs(x_atual-x_ant/x_atual) * 100
        
        x_atual = g(x_ant)
        
        it += 1
        
    return x_atual, erro, it
    
    
x_aproximado, erro_final, iteracoes = PontoFixo(g, 2, 0.0001, 100)
print(f"Raiz aproximada: {x_aproximado}")
print(f"Erro: {erro_final:.6f}%")
print(f"Iterações: {iteracoes}")
    
    
