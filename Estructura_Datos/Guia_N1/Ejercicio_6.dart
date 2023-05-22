import 'dart:math';
List<int> multiplicar(List<int> lista1, List<int> lista2) {
  // assert(lista1.length == lista2.length);    [comprobación largo de listas para poder multiplicar]
  List<int> resultado = [];
  for (int i = 0; i < lista1.length; i++) {   // lista1.length = 5 para este caso
    resultado.add(lista1[i] * lista2[i]);
  }
  return resultado;
}
// Generar lista según el largo indicado y que posea elementos comprendidos entre los numeros dados
List<int> generarNegativos(int length, int min, int max) {
  List<int> lista = [];
  for (int i = 0; i < length; i++) {
    int numeroAleatorio = min + Random().nextInt(max - min + 1);
    lista.add(numeroAleatorio);
  }
  return lista;
}

void main() {
  print('Multiplicar listas, concatenar con otra lista negativa y ordenar descendentemente');
  // Definir las dos listas a multiplicar
  List<int> lista1 = [4, 3, 2, 2, 1];
  List<int> lista2 = [-3, 2, 8, 0, 1];
  // Multiplicar las dos listas
  List<int> resultado = multiplicar(lista1, lista2);
  print('Resultado de la multiplicación:\n$resultado');
  // Generar la lista aleatoria de números negativos
  List<int> listaAleatoria = generarNegativos(5, -5, -1);
  print('Lista aleatoria de números negativos:\n$listaAleatoria');
  // Concatenar el resultado de la multiplicación con la lista aleatoria
  List<int> listaConcatenada = [...resultado, ...listaAleatoria];
  print('Lista concatenada:\n$listaConcatenada');
  // Ordenar la lista de forma descendente
  listaConcatenada.sort((a, b) => b.compareTo(a));
  print('Lista ordenada de forma descendente:\n$listaConcatenada');
}