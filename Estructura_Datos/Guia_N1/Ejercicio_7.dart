void main() {
  print('Crear una lista de carácteres y números e imprimir únicamente los números');
  // Definimos la lista
  List<dynamic> lista = ['a', 2, 0, 'b', 8, 'c'];

  // Filtramos la lista únicamente para números enteros
  List<int> numero = [];
  for (var elemento in lista) {
    if (elemento is int) {
      numero.add(elemento);
    }
  }
  print('Números filtrados por un bucle:\n$numero');

  // Otra manera de filtrar la lista
  List<int> numeros = lista.whereType<int>().toList();

  print('Números filtrados por funciones:\n$numeros');
}