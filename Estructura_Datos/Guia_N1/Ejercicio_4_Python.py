import random
import numpy as np

#Se genera una matriz aleatoria de 3 a 5
dimension = random.randint(3, 5)
matriz_original = np.random.randint(1, 10, size=(dimension, dimension))

#Se imprime la matriz original
print("La matriz original es:")
print(matriz_original)

#Se calcula la matriz inversa utilizando la libreria numpy
matriz_inversa = np.linalg.inv(matriz_original)

#Se imprime la matriz inversa
print("La matriz inversa es:")
print(matriz_inversa)