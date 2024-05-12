## Factorizacion LU

import numpy as np

dim_A = int(input("Ingrese la dimensión de la matriz cuadrada A: "))
A = np.zeros((dim_A, dim_A))
for i in range(dim_A):
    for j in range(dim_A):
        A[i, j] = float(input(f"Ingrese el elemento A[{i + 1}, {j + 1}]: "))

print(f"\nLa matriz A es:\n{A}")

# Factorizacion LU
L = np.eye(dim_A)
U = np.zeros((dim_A, dim_A))

for k in range(dim_A):
    U[k, k] = A[k, k] - np.dot(L[k, :k], U[:k, k])
    for i in range(k + 1, dim_A):
        L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]
    for j in range(k + 1, dim_A):
        U[k, j] = A[k, j] - np.dot(L[k, :k], U[:k, j])

print(f"\nLa matriz L es:\n{L}")
print(f"\nLa matriz U es:\n{U}")