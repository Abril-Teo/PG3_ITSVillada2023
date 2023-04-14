class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        if self.nota >= 6:
            print (f"El alumno {self.nombre} tiene una nota de {self.nota}, por lo tanto queda APROBADO")
        else:
            print (f"El alumno {self.nombre} tiene una nota de {self.nota}, por lo tanto queda DESAPROBADO")

nombre = (input("Ingrese nombre del alumno 1 >>> "))
nota = float(input("Ingrese la nota del alumno 1 >>> "))
alumno1 = Alumno(nombre, nota)
alumno1.mostrar()

nombre = (input("Ingrese nombre del alumno 1 >>> "))
nota = float(input("Ingrese la nota del alumno 1 >>> "))
alumno2 = Alumno(nombre, nota)
alumno2.mostrar()