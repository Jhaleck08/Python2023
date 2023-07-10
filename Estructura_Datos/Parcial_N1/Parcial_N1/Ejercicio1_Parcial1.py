import numpy as np
from random import randint

#Se genera una matriz de 3x3 con valores a y b
a=5
b=10
matriz=np.zeros((3,3))
for i in range(3):
   for j in range(3):
    matriz[i,j]=randint(a,b)
print("La matriz creada es:\n")
print(matriz)

#Obtener la determinante
determinante=np.linalg.det(matriz)
print("El determinante de la matriz es:\n" ,determinante)


