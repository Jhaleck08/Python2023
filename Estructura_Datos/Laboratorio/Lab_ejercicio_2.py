
import random
columna=[]
fila=[]
numero_columnas=int(2)
numero_filas=int(1)

#Crear la función crear_matriz para así poder crear una matriz
def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(1, 5))
        matriz.append(fila)
    return matriz


