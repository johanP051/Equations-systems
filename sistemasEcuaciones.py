import numpy as np

class SistemaEcuaciones:
    def __init__(self, ecuaciones, variables):
        self.ecuaciones = ecuaciones
        self.variables = variables
        self.filas = []
        self.matrizReducir = None

    def recoger_datos(self):
        for i in range(self.ecuaciones):
            elementosFila = []
            print(f"\nPara la ecuación número {i + 1}:")

            for j in range(self.variables):
                Xn = int(input(f"Inserte el valor de X{j + 1}: "))
                elementosFila.extend([Xn])

            igualdad = int(input(f"¿A qué valor está igualada la ecuación?: "))
            elementosFila.extend([igualdad])

            self.filas.append(elementosFila)

    def resolver(self):
        if self.ecuaciones != self.variables:
            print("El sistema no se puede solucionar porque el número de ecuaciones es diferente al número de variables.")
            return

        mAumentada = np.array(self.filas, dtype='float')
        print(f"\nLa matriz aumentada es:\n\n{mAumentada}")

        self.matrizReducir = mAumentada.copy()

        print("\nPrimera parte del Gauss-Jordan\n")
        self.gauss_jordan()

    def gauss_jordan(self):
        inicioFilaSimplificacion = -1
        finalFilaSimplificacion = self.ecuaciones
        elementoFilaSimplificacion = -1

        inicioFilaReduccion = 0
        finalFilaReduccion = self.ecuaciones
        filaPivote = -1

        columnas = self.variables

        while columnas >= 1:
            inicioFilaSimplificacion += 1
            finalFS = finalFilaSimplificacion
            elementoFilaSimplificacion += 1

            for filaS in range(inicioFilaSimplificacion, finalFS):
                filaSimplificada = self.matrizReducir[filaS]
                filaSimplificada = filaSimplificada / filaSimplificada[elementoFilaSimplificacion]
                self.matrizReducir[filaS] = filaSimplificada

            print(f"\nResultado de la simplificación: ")
            print(self.matrizReducir)

            inicioFilaReduccion += 1
            finalFR = finalFilaReduccion
            filaPivote += 1

            for filaR in range(inicioFilaReduccion, finalFR):
                filaReducida = self.matrizReducir[filaR]
                filaReducida = filaReducida - self.matrizReducir[filaPivote]
                self.matrizReducir[filaR] = filaReducida

            print(f"\nResultado de la Reducción: \n{self.matrizReducir}")

            columnas -= 1

        print("\nSegunda parte del Gauss Jordan:")
        self.gauss_jordan_segunda_parte()

    def gauss_jordan_segunda_parte(self):
        inicioFilaSimplificacion = 0
        finalFilaSimplificacion = self.ecuaciones
        elementoFilaSimplificacion = self.variables

        inicioFilaReduccion = 0
        finalFilaReduccion = self.ecuaciones
        filaPivote = self.ecuaciones

        columnas = self.variables

        while columnas >= 1:
            inicioFS = inicioFilaSimplificacion
            finalFilaSimplificacion -= 1
            elementoFilaSimplificacion -= 1

            for filaS in reversed(range(inicioFS, finalFilaSimplificacion + 1)):
                filaSimplificada = self.matrizReducir[filaS]
                filaSimplificada = filaSimplificada / filaSimplificada[elementoFilaSimplificacion]
                self.matrizReducir[filaS] = filaSimplificada

            print(f"\nResultado de la simplificación: ")
            print(self.matrizReducir)

            inicioFR = inicioFilaReduccion
            finalFilaReduccion -= 1
            filaPivote -= 1

            for filaR in reversed(range(inicioFR, finalFilaReduccion)):
                filaReducida = self.matrizReducir[filaR]
                filaReducida = filaReducida - self.matrizReducir[filaPivote]
                self.matrizReducir[filaR] = filaReducida

            print(f"\nResultado de la Reducción: \n{self.matrizReducir}")
            columnas -= 1

ecuaciones = int(input("Inserte el número de ecuaciones: "))
variables = int(input("Inserte el número de variables: "))

sistema = SistemaEcuaciones(ecuaciones, variables)
sistema.recoger_datos()
sistema.resolver()