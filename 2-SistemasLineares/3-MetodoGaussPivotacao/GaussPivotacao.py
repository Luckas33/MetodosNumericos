import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '1-Determinantes')))
import retroativas


def GaussPivotacao(A, b):
    n = len(A)

    for k in range(n - 1):
        max_row = max(range(k, n), key=lambda i: abs(A[i][k]))
        if A[max_row][k] == 0:
            raise ValueError("Matriz singular - divisão por zero detectada.")
        
        if max_row != k:
            A[k], A[max_row] = A[max_row], A[k]
            b[k], b[max_row] = b[max_row], b[k]

        for i in range(k + 1, n):
            m = -A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] = m * A[k][j] + A[i][j]
            b[i] = m * b[k] + b[i]
            A[i][k] = 0

    x = retroativas.subs_retroativas(A, b)
    return x

if __name__ == "__main__":
    A = [
        [1, -3, 2],
        [-2, 8, -1],
        [4, -6, 5]
    ]
    b = [11, -15, 29]

    x = GaussPivotacao(A, b)
    print("Solução:", x)