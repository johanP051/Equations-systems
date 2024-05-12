import numpy as np

class SistemaEcuaciones:
    def __init__(self, ecuaciones, variables):
        self.ecuaciones = ecuaciones
        self.variables = variables
        
        # Lista para almacenar las filas de la matriz
        self.filas = []
        # Matriz para realizar las operaciones de Gauss-Jordan
        self.matrizReducir = None

    def recoger_datos(self):
        for i in range(self.ecuaciones):
            elementosFila = []
            print(f"\nPara la ecuación número {i + 1}:")

            for j in range(self.variables):
                Xn = int(input(f"Inserte el valor del coeficiente X{j + 1}: "))
                elementosFila.extend([Xn])

            igualdad = int(input(f"¿A qué valor está igualada la ecuación?: "))
            elementosFila.extend([igualdad])

            # Agregar la fila a la lista de filas, cada fila representa un solo elemento de la lista
            #para que después se pueda crear un arreglo de numpy
            self.filas.append(elementosFila)

    def resolver(self):
        if self.ecuaciones != self.variables:
            print("\n No puedo solucionar sistemas de ecuaciones que no tengan el mismo número de ecuaciones y variables.")
            return

        mAumentada = np.array(self.filas, dtype='float')  # Crear la matriz aumentada
        print(f"\nLa matriz aumentada es:\n\n{mAumentada}")

        self.matrizReducir = mAumentada.copy()  # Copiar la matriz aumentada a la matriz de reducción

        print("\nPrimera parte del Gauss-Jordan\n")
        self.gauss_jordan()  # Realizar la primera parte del algoritmo de Gauss-Jordan

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
            #print(inicioFilaSimplificacion, finalFS, elementoFilaSimplificacion)
            # Simplificar la fila actual dividiendo por el elemento de la columna correspondiente
            for filaS in range(inicioFilaSimplificacion, finalFS):
                filaSimplificada = self.matrizReducir[filaS]
                if filaSimplificada[elementoFilaSimplificacion] != 0:
                    filaSimplificada = filaSimplificada / filaSimplificada[elementoFilaSimplificacion]
                self.matrizReducir[filaS] = filaSimplificada

            print(f"\nResultado de la simplificación: ")
            print(self.matrizReducir)

            inicioFilaReduccion += 1
            finalFR = finalFilaReduccion
            filaPivote += 1
            #print(inicioFilaReduccion, finalFR, filaPivote)
            # Reducir las filas restantes restando la fila pivote multiplicada por el elemento correspondiente
            for filaR in range(inicioFilaReduccion, finalFR):
                filaReducida = self.matrizReducir[filaR]
                if filaReducida[filaPivote] != 0:
                    filaReducida = filaReducida - self.matrizReducir[filaPivote]
                self.matrizReducir[filaR] = filaReducida

            print(f"\nResultado de la Reducción: \n{self.matrizReducir}")

            columnas -= 1

        print("\nSegunda parte del Gauss Jordan:")
        self.gauss_jordan_segunda_parte()  # Realizar la segunda parte del algoritmo de Gauss-Jordan

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

            # Simplificar la fila actual dividiendo por el elemento de la columna correspondiente
            for filaS in reversed(range(inicioFS, finalFilaSimplificacion + 1)):
                filaSimplificada = self.matrizReducir[filaS]
                if filaSimplificada[elementoFilaSimplificacion] != 0:
                    filaSimplificada = filaSimplificada / filaSimplificada[elementoFilaSimplificacion]
                self.matrizReducir[filaS] = filaSimplificada

            print(f"\nResultado de la simplificación: ")
            print(self.matrizReducir)

            inicioFR = inicioFilaReduccion
            finalFilaReduccion -= 1
            filaPivote -= 1

            # Reducir las filas restantes restando la fila pivote multiplicada por el elemento correspondiente
            for filaR in reversed(range(inicioFR, finalFilaReduccion)):
                filaReducida = self.matrizReducir[filaR]
                if filaReducida[filaPivote] != 0:
                    filaReducida = filaReducida - self.matrizReducir[filaPivote]
                self.matrizReducir[filaR] = filaReducida

            print(f"\nResultado de la Reducción: \n{self.matrizReducir}")
            columnas -= 1

# Solicitar el número de ecuaciones y variables al usuario
ecuaciones = int(input("Inserte el número de ecuaciones: "))
variables = int(input("Inserte el número de variables: "))

# Crear una instancia de la clase SistemaEcuaciones y resolver el sistema
sistema = SistemaEcuaciones(ecuaciones, variables)
sistema.recoger_datos()
sistema.resolver()
