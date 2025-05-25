import numpy as np

a = [1,-3,7,5-2,3]
n = len(a)-1
b = a[n]

def horner(b, z , a):
    for j in range (n - 1, -1 ,-1):
        b = a[j] + b*z
    
    return b

print(horner(b,2,a))