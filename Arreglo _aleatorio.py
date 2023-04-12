
import array

#Generamos un arreglo aleatorio de enteros de tamaño 10
arreglo = array.array('i', [1, 5, 9, 2, 3, 7, 8, 4, 6, 0])

#Imprimimos el arreglo generado
print("Arreglo generado:", arreglo)

#Se solicita al usuario que ingrese un número a buscar
numero_buscar = int(input("Ingrese un número a buscar en el arreglo: "))

#Buscamos el número en el arreglo y mostramos el resultado
if numero_buscar in arreglo:
    print(f"El número {numero_buscar} se encuentra en el arreglo.")
else:
    print(f"El número {numero_buscar} no se encuentra en el arreglo.")