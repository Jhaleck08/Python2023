class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.Subordinados = []

class Empresa:
    def __init__(self):
        self.raiz = None

    def nuevoEmpleado(self, nombreEmpleado, cargo, Jefecito=None):
        empleado = Empleado(nombreEmpleado, cargo)
        if Jefecito:
            Jefecito.Subordinados.append(empleado)
        else:
            self.raiz = empleado

    def unEmpleadomenos(self, nombre):
        empleado = self.PosibleEmpleado(nombre)
        if empleado:
            jefecito = self.nuevoJefecito(empleado)
            jefecito.Subordinados.extend(empleado.Subordinados)
            jefecito.Subordinados.remove(empleado)

    def Jerarquia(self):
        self.verEmpleado(self.raiz, 0)

    def PosibleEmpleado(self, nombre, empleado=None):
        if empleado is None:
            empleado = self.raiz
        if empleado:
            if empleado.nombreEmpleado == nombre:
                return empleado
            for subordinado in empleado.Subordinados:
                encontrado = self.PosibleEmpleado(nombre, subordinado)
                if encontrado:
                    return encontrado
        return None

    def nuevoJefecito(self, empleado, jefecito=None):
        if jefecito is None:
            jefecito = self.raiz
        if jefecito:
            if empleado in jefecito.Subordinados:
                return jefecito
            for subordinado in jefecito.Subordinados:
                encontrado = self.nuevoJefecito(empleado, subordinado)
                if encontrado:
                    return encontrado
        return None

    def verEmpleado(self, empleado, nivel):
        if empleado:
            print("  " * nivel + f"{empleado.nombre} - {empleado.cargo}")
            for subordinado in empleado.Subordinados:
                self.verEmpleado(subordinado, nivel + 1)

    def buscarEmpleado(self, nombre, empleado):
        if empleado:
            if empleado.nombreEmpleado == nombre:
                return empleado
            for subordinado in empleado.Subordinados:
                encontrado = self.buscarEmpleado(nombre, subordinado)
                if encontrado:
                    return encontrado
        return None

    def buscarJefecito(self, empleado, jefecito):
        if jefecito:
            if empleado in jefecito.Subordinados:
                return jefecito
            for subordinado in jefecito.Subordinados:
                encontrado = self.buscarJefecito(empleado, subordinado)
                if encontrado:
                    return encontrado
        return None

empresa = Empresa()

empresa.nuevoEmpleado("CEO", "Director Ejecutivo")
empresa.nuevoEmpleado("Gerente", "Gerente General", empresa.raiz)
empresa.nuevoEmpleado("Empleado1", "Empleado", empresa.raiz.Subordinados[0])
empresa.nuevoEmpleado("Empleado2", "Empleado", empresa.raiz.Subordinados[0])
empresa.nuevoEmpleado("Empleado3", "Empleado", empresa.raiz.Subordinados[0])
empresa.nuevoEmpleado("Empleado4", "Empleado", empresa.raiz.Subordinados[0]) 

empresa.Jerarquia()
