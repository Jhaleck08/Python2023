import 'dart:math';

// Generar lista según el largo indicado y que posea elementos comprendidos entre los numeros dados
List<int> generarLista(int largo, int min, int max) {
  List<int> lista = [];
  for (int i = 0; i < largo; i++) {
    int numeroAleatorio = min + Random().nextInt(max - min + 1);
    lista.add(numeroAleatorio);
  }
  return lista;
}
// Sumar las listas generadas y luego retornar el resultado dividido por el largo de esta
double promedio(List<int> lista) {
  int suma = 0;
  for (int numero in lista) {
    suma += numero;
  }
  return suma / lista.length;
}

void main() {
  print('Obtener el promedio de tres listas diferentes de 7 elementos cada una. Los elementos de estas listas se generan de forma aleatoria (elementos del 30 al 100). Guardar los promedios obtenidos en una nueva lista.\n');

  // Generar las tres listas con elementos aleatorios (largo, mínimo y máximo)
  List<int> lista1 = generarLista(7, 30, 100);
  List<int> lista2 = generarLista(7, 30, 100);
  List<int> lista3 = generarLista(7, 30, 100);

  // Imprimir las listas generadas
  print('Lista 1: $lista1');
  print('Lista 2: $lista2');
  print('Lista 3: $lista3');

  // Calcular el promedio de cada lista
  List<double> promedios = [
    promedio(lista1),
    promedio(lista2),
    promedio(lista3)
  ];

  // Imprimir los promedios obtenidos
  print('\nPromedios: $promedios');
}