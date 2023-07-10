#Letra A
class contacto_telefónico:
    def __init__(self,nombre_contacto,número_telefono,correo_electrónico):
        self.nombre_contacto=nombre_contacto
        self.número_telefono=número_telefono
        self.correo_electrónico=correo_electrónico
        self.siguiente=None
        self.anterior=None

class lista_contactos:
    def __init__(self):
        self.inicio=None
  
    #Letra B
    def agregar_contacto_telefónico(self,nombre_contacto,número_telefono,correo_electrónico):
        contacto_nuevo=contacto_telefónico(nombre_contacto,número_telefono,correo_electrónico)

        if self.inicio is None:
            self.inicio=contacto_nuevo
            contacto_nuevo.siguiente=contacto_nuevo
            contacto_nuevo.anterior=contacto_nuevo
        else:
            ultimo_contacto=self.inicio.anterior
            contacto_nuevo.siguiente=self.inicio
            contacto_nuevo.anterior=ultimo_contacto
            self.inicio.anterior=contacto_nuevo
            ultimo_contacto.siguiente=contacto_nuevo
    
    #Letra C
    def mostrar_lista_contactos(self):
        contacto=self.inicio
        while contacto:
            print("El nombre del contacto es: \n", contacto.nombre_contacto)
            print("El número telefónico es: \n", contacto.número_telefono)
            print("El correo eléctronico del contacto es: \n", contacto.correo_electrónico)
            contacto=contacto.siguiente        
    
    #Letra D
    def buscar_contacto(self,nombre_contacto):
        contacto=self.inicio
        while contacto:
            if contacto.nombre_contacto==nombre_contacto:
                return contacto
            contacto=contacto.siguiente
            return None


