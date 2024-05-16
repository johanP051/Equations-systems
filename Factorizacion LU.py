import numpy as np

dim_A = int(input("Ingrese la dimensión de la matriz cuadrada A: "))
A = np.zeros((dim_A, dim_A))

for i in range(dim_A):
    for j in range(dim_A):
        A[i, j] = float(input(f"Ingrese el elemento A[{i + 1}, {j + 1}]: "))


# Factorizacion LU
L = np.identity(dim_A)
U = A.copy()

for j in range(dim_A):
    for i in range(j+1, dim_A):
        # Factor que multiplica a la fila j para igualarlo al elemneto [i, j] de la matriz U y que al restarlos dé 0
        factor = U[i, j] / U[j, j]

        #Se actualiza la matriz L con el factor
        L[i, j] = factor
        #Se reduce la fila i de la matriz U
        U[i] = U[i] - factor * U[j]

print(f"\nMatriz A: \n{A}\n\n Matriz L: \n{L}\n\n Matriz U: \n{U}\n")

print("Verificación: L * U = A")
print(np.dot(L, U))