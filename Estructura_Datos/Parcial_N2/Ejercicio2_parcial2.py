class Producto:
    def __init__(self, código, nombre_producto, descripción_producto, cantidad_producto):
        self.código=código
        self.nombre_producto=nombre_producto
        self.descripción_producto=descripción_producto
        self.cantidad_producto=cantidad_producto
        self.siguiente=None
        self.anterior=None

class Inventario:
    def __init__(self):
        self.primer_producto=None
        self.ultimo_producto=None

    #Letra A
    def agregar_producto(self, código, nombre_producto, descripción_producto, cantidad_producto):
        nuevo_producto=Producto(código, nombre_producto, descripción_producto, cantidad_producto)

        if self.primer_producto is None:
            self.primer_producto=nuevo_producto
            self.ultimo_producto=nuevo_producto
        else:
            nuevo_producto.anterior=self.ultimo_producto
            self.ultimo_producto.siguiente=nuevo_producto
            self.ultimo_producto=nuevo_producto

    #Letra B
    def eliminar_producto(self,código):
        producto=self.primer_producto
        while producto:
            if producto.código==código:
                if producto.anterior:
                    producto.anterior.siguiente=producto.siguiente
                else:
                    self.primer_producto=producto.siguiente

                if producto.siguiente:
                    producto.siguiente.anterior=producto.anterior
                else:
                    self.ultimo_producto=producto.anterior

                del producto
                break
            producto=producto.siguiente

    #Letra C
    def buscar_producto(self, código):
        producto=self.primer_producto
        while producto:
            if producto.código==código:
                return producto
            producto=producto.siguiente
        return None
    
    #Letra D
    def actualizar_cantidad_producto(self, código, cantidad_nueva):
        producto=self.buscar_producto(código)
        if producto:
            producto.cantidad=cantidad_nueva
    
    #Letra E
    def mostrar_producto(self):
        producto=self.primer_producto
        while producto:
            print("El código del producto es: \n",producto.código)
            print("El nombre del producto es: \n", producto.nombre_producto)
            print("Descripción del producto: \n", producto.descripción_producto)
            print("La cantidad que se encuentra disponible del producto es/son: \n", producto.cantidad_producto)
            producto=producto.siguiente

inventario=Inventario()

inventario.agregar_producto("015", "Manzanas", "Malla de manzanas de 1 kg", 4)
inventario.agregar_producto("090", "Pan", "Bolsa de pan", 15)
inventario.agregar_producto("088", "Galletas", "Todo tipo de galletas", 10)
inventario.agregar_producto("010", "Leche", "Leche semidescremada, entera o descremada", "30")
#Aquí se muestran todos los productos del inventario
inventario.mostrar_producto()

#Aquí se busca un producto
producto=inventario.buscar_producto("090")
if producto is not None:
    print("El producto ha sido encontrado")
    print("El código del producto es: \n", producto.código)
    print("El nombre del producto es: \n", producto.nombre_producto)
    print("Descripción del producto: \n ", producto.descripción_producto)
    print("Cantidad del producto: \n ", producto.cantidad_producto)
else:
    print("El producto no fue encontrado")

#Aquí es para actualizar la cantidad del producto o de los productos
inventario.actualizar_cantidad_producto("010", 40)

#Se muestran todos los productos que se encuentran en el inventario
inventario.mostrar_producto()

#Se elimina un producto
inventario.eliminar_producto("010")

#Se muestran los productos después de que se haya eliminado uno
inventario.mostrar_producto()










    
