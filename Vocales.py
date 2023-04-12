
palabra = input("Ingrese una palabra: ")
vocales = "aeiou"

#Se crea un diccionario para almacenar cuantas veces aparece la vocal en la palabra
vocales_contador = {v: 0 for v in vocales}

for letra in palabra:
    if letra.lower() in vocales:
        vocales_contador[letra.lower()] += 1

#Se muestran los resultados
for vocal, contador in vocales_contador.items():
    print(f"La vocal {vocal} aparece {contador} veces en la palabra.")
