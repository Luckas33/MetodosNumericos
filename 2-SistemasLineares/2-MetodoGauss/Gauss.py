import numpy as np

def subs_retroativas(A,b):
    n = len(A)
    x = n * [n]

    for i in range(n-1,-1,-1):
        S = 0
        for j in range(i+1,n):
            S = S + A[i][j] * x[j]
        x[i] = (b[i] - S) / A[i][i]    
    
    return x

def Gauss(A,b):
    n = len(A)
    
    for k in range (0, n-1):
        for i in range (k+1,n):
            m = -A[i][k]/A[k][k]
            for j in range (k+1,n):
                A[i][j] = m * A[k][j] + A[i][j]
            
            b[i] = m * b[k] + b[i]
            
            A[i][k] = 0
        
    x = subs_retroativas(A,b)   
    return x


A1 = [
    [1,-3,2],
    [-2,8,-1],
    [4,-6,5]
    ]

b1 = [11,-15,29]

x = Gauss(A1,b1)
print(x)