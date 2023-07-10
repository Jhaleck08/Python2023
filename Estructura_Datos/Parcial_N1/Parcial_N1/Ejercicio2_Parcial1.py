import numpy as np
import random

#Crear matrices
filas=[3]
columnas=[3]

matriz_1=[]
for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(random.randint(-5,-10))
        matriz_1.append(fila)

matriz_2=[]
for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(random.randint(-5,-10))
        matriz_2.append(fila)

#Multiplicar ambas matrices
matriz_multiplicación=[]
for i in range(filas):
    fila=[]
    for j in range(columnas):
        multiplicación=matriz_1[i][j] * matriz_2[i][j]
        fila.append(multiplicación)
        matriz_multiplicación.append(fila)

#Imprimir el resultado de la multiplicación de las dos matrices
print("El valor de la multiplicación de las dos matrices es:\n")
for fila in matriz_multiplicación:
    print(fila)

#Crear nueva matriz
filas=[3]
columnas=[3]

matriz_3=[]
for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(random.randint(-5,-10))
        matriz_3.append(fila)

#Multiplicar la matriz creada por el resultado de la multiplicación de las dos primeras matrices
resultado_matriz_final=np.array(matriz_multiplicación)*matriz_3

#Se imprime el resultado de la matriz final
print("El resultado de la matriz final es:\n")
print(matriz_3)


        