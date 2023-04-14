class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print("Su nombre es ", self.nombre)

Persona1 = Persona(input("Ingrese el nombre 1 >>> "))
Persona1.mostrar()

Persona2 = Persona(input("Ingrese el nombre 2 >>> "))
Persona2.mostrar()
