class Operaciones:
    def __init__(self):
        self.num1 = int(input("Ingrese un numero entero >>> "))
        self.num2 = int(input("Ingrese otro numero entero >>> "))
        Operaciones.suma(self)
        Operaciones.resta(self)
        Operaciones.divicion(self)
        Operaciones.multiplicacion(self)
        
    def suma(self):
        print(f"Suma = {self.num1 + self.num2}")
    
    def resta(self):
        print(f"Resta = {self.num1 - self.num2}")

    def multiplicacion(self):
        print(f"Multiplicación = {self.num1 * self.num2}")

    def divicion(self):
        if self.num2 != 0:
            print(f"Division: {self.num1 / self.num2}")
        else:
            print("Division: No se puede didvir por 0")

op = Operaciones()