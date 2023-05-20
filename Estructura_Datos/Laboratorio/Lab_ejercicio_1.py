
import array
import random

#Le damos un valor para que nos dé una cantidad de filas y columnas
numero_filas = int(input("Ingrese cantidad de filas:\n"))
numero_columnas = int(input("Ingrese cantidad de columnas:\n"))
fila = []
columna = []

#Crear la primera matriz mediante un ciclo
matriz_1=[]
for i in range(numero_filas):   
    fila = array.array('i', (random.randrange(1, 6) for j in range(numero_columnas)))
    matriz_1.append(fila)

#Crear la segunda matriz mediante un ciclo
matriz_2 = []
for i in range(numero_filas):
    fila = array.array('i', (random.randrange(1, 6) for j in range(numero_columnas)))
    matriz_2.append(fila)

#Creamos la función sumar_matrices para las dos matrices
def sumar_matrices(matriz_1, matriz_2):
    resultado = []
    for i in range(numero_filas):
        fila = array.array('i', (matriz_1[i][j] + matriz_2[i][j] for j in range(numero_columnas)))
        resultado.append(fila)
    return resultado

#Creamos la función restar_matrices para las dos matrices
def restar_matrices(matriz_1, matriz_2):
    resultado = []
    for i in range(numero_filas):
        fila = array.array('i', (matriz_1[i][j] - matriz_2[i][j] for j in range(numero_columnas)))
        resultado.append(fila)
    return resultado
    
    

