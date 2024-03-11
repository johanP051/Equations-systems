import numpy as np
import pandas as pd

ecuaciones = int(input("Inserte el número de ecuaciones: "))
variables = int(input("Inserte el número de variables: "))

filas = []

for i in range(ecuaciones):
    elementosFila = []
    print(f"\nPara la ecuación número {i + 1}:")

    for j in range(variables):
        Xn = int(input(f"Inserte el valor de X{j + 1}: "))
        elementosFila.extend([Xn])

    igualdad = int(input(f"¿A qué valor está igualada la ecuación?: "))
    elementosFila.extend([igualdad])

    filas.append(elementosFila)


mAumentada = np.array(filas, dtype='float')
print(f"\nLa matriz aumentada es:\n\n{mAumentada}")

matrizReducir = mAumentada.copy()

print("\nPrimera parte del Gauss-Jordan\n")

inicioFilaSimplificacion = -1
finalFilaSimplificacion = ecuaciones
elementoFilaSimplificacion = -1

inicioFilaReduccion = 0
finalFilaReduccion = ecuaciones
filaPivote = -1

columnas = variables


while columnas >= 1:
    inicioFilaSimplificacion += 1
    finalFS = finalFilaSimplificacion
    elementoFilaSimplificacion += 1

    for filaS in range(inicioFilaSimplificacion, finalFS):
        filaSimplificada = matrizReducir[filaS]
        filaSimplificada = filaSimplificada / filaSimplificada[elementoFilaSimplificacion]
        matrizReducir[filaS] = filaSimplificada

    print(f"\nResultado de la simplificación: ")
    print(matrizReducir)


    inicioFilaReduccion += 1
    finalFR = finalFilaReduccion
    filaPivote += 1

    for filaR in range(inicioFilaReduccion, finalFR):
        filaReducida = matrizReducir[filaR]
        filaReducida = filaReducida - matrizReducir[filaPivote]
        matrizReducir[filaR] = filaReducida

    print(f"\nResultado de la Reducción: \n{matrizReducir}")

    columnas -= 1

print("\nSegunda parte del Gauss Jordan:")

inicioFilaSimplificacion = 0
finalFilaSimplificacion = ecuaciones
elementoFilaSimplificacion = variables

inicioFilaReduccion = 0 #constante
finalFilaReduccion = ecuaciones
filaPivote = ecuaciones

columnas = variables

while columnas >= 1:
    
    inicioFS = inicioFilaSimplificacion
    finalFilaSimplificacion -= 1
    elementoFilaSimplificacion -= 1
    print(f"e.Simplificacion: {elementoFilaSimplificacion}")

    for filaS in reversed(range(inicioFS, finalFilaSimplificacion + 1)):
        filaSimplificada = matrizReducir[filaS]
        print(f"fila a simplificar: {filaSimplificada}")
        filaSimplificada = filaSimplificada / filaSimplificada[elementoFilaSimplificacion]
        matrizReducir[filaS] = filaSimplificada

    print(f"\nResultado de la simplificación: ")
    print(matrizReducir)

    #Por cual fila voy a a empezar a reducir?
    inicioFR = inicioFilaReduccion
    #En cual fila voy a terminar de reducir?
    finalFilaReduccion -= 1
    #Qué fila voy a usar para reducir?
    filaPivote -= 1

    # Va de 0 hasta finalFilaReduccion - 1, en caso de dos ecuaciones va de 0 a 1, pero como no incluye al 1, entonces solo va de 0 a 0
    for filaR in reversed(range(inicioFR, finalFilaReduccion)):
        #filaR = finalFR - 1 - 1
        filaReducida = matrizReducir[filaR]
        filaReducida = filaReducida - matrizReducir[filaPivote]
        #print(f"Indice: {filaR}, reduccion de la fila: {filaReducida}")
        matrizReducir[filaR] = filaReducida

    print(f"\nResultado de la Reducción: \n{matrizReducir}")
    columnas -= 1



