def GaussJordan(A, b):
    n = len(A)

    for k in range(n):
        if A[k][k] == 0:
            for i in range(k + 1, n):
                if A[i][k] != 0:
                    A[k], A[i] = A[i], A[k]
                    b[k], b[i] = b[i], b[k]
                    break
            else:
                raise ValueError("Matriz singular - não é possível resolver.")

        pivô = A[k][k]
        for j in range(n):
            A[k][j] = A[k][j] / pivô
        b[k] = b[k] / pivô

        for i in range(n):
            if i != k:
                fator = A[i][k]
                for j in range(n):
                    A[i][j] -= fator * A[k][j]
                b[i] -= fator * b[k]

    return b 