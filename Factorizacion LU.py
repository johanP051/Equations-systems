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
U = A.copy()

k = 0
#pivote = U[k, k]
inicioFilaReducir = 1
finalFIlaReducir = dim_A

for j in range(dim_A):
    pivote = U[j, j]
    for i in range(inicioFilaReducir, finalFIlaReducir):
        print(f"\n\nU[j] = {U[j]} \n\n Pivote: {pivote} \n\n U[i, j] = {U[i, j]} \n\n U[i] = {U[i]}")
        filaReducida = U[j] - ((pivote / U[i, j]) * U[i])
        U[i] = filaReducida
        #print(filaReducida)
    inicioFilaReducir += 1
    print(U)
print(A)
print(U)
    