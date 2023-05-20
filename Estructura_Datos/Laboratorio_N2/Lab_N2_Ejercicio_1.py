import random
import numpy as np

#Se le pide al usuario que agregue la cantidad de filas y columnas
filas=int(input("Ingrese un valor para la cantidad de filas:\n"))
columnas=int(input("Ingrese un valor para la cantidad de columnas:\n"))

#Se crean las dos matrices
matriz_1=[]
for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(random.randint(1,5))
    matriz_1.append(fila)

matriz_2=[]
for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(random.randint(1,5))
    matriz_2.append(fila)

#Se suman las dos matrices
matriz_suma=[]
for i in range(filas):
    fila=[]
    for j in range(columnas):
        suma=matriz_1[i][j] + matriz_2[i][j]
        fila.append(suma)
    matriz_suma.append(fila)

#Resultado de la suma de las dos matrices
print("El valor de la suma de las dos matrices es:\n")
for fila in matriz_suma:
    print(fila)

#Se le pide al usuario que ingrese valor para el escalar
escalar=int(input("Ingrese un valor para el escalar:\n"))
resultado_matriz_multiplicación=np.array(matriz_suma)*escalar

#Se imprime el resultado
print("El resultado de la multiplicación mediante el escalar es:\n")
print(resultado_matriz_multiplicación)

#Se le pide la usuario que ingrese valor para la cantidad de filas y columnas de la nueva matriz
filas_nueva_matriz=int(input("Ingrese un valor para la cantidad de filas:\n"))
columnas_nueva_matriz=int(input("Ingrese un valor para la cantidad de columnas:\n"))

#Se crea la nueva matriz
matriz_3=[]
for i in range(filas_nueva_matriz):
    fila=[]
    for j in range(columnas_nueva_matriz):
        fila.append(random.randint(1,5))
    matriz_2.append(fila)

ultimo_resultado_matriz=np.array(resultado_matriz_multiplicación, matriz_3)

#Se imprime el resultado de la última matriz
print("El resultado final de la última matriz es:\n")
print(matriz_3)




