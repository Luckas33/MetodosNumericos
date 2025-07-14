import math
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


A=[
    [5, -2, 6, 1],
    [0, 3, 7, -4],
    [0, 0, 4, 5],
    [0, 0, 0, 2]
   ]

b = [1,-2,28,8]

x = subs_retroativas(A,b)
print(x)