#crear matriz
matriz_1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]

#suma de cada columna
suma_de_columna = [sum(matriz_1[columna][filas] 
                   
    for columna in range(len(matriz_1))) 

        for filas in range(len(matriz_1[0]))]

#suma más alta
suma_alta_columna = max(suma_de_columna)

#suma de cada fila
suma_de_filas = [sum(filas) for filas in matriz_1]

#suma baja de las filas
suma_baja_filas = min(suma_de_filas)

print("La suma mas alta de las columnas es:", suma_alta_columna)
print("La suma mas baja de las filas es:", suma_baja_filas)