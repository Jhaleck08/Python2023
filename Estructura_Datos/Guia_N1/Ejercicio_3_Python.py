import numpy as np
from random import randint

#se genera una matriz de 3x3
a = 1
b = 10
matriz = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        matriz[i, j] = randint(a, b)
print("La matriz es:")
print(matriz)

#calcular y obtener resultado de la determinante
determinante = np.linalg.det(matriz)
print("El determinante es:", determinante)
