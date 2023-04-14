class Familia:
    def __init__(self, nomPadre, nomMadre, nomHijos):
        self.padre = nomPadre
        self.madre = nomMadre
        self.hijos = nomHijos
    
    def __str__(self):
        return f"""
        Padre:{self.padre} 

        Madre: {self.madre}

        Hijos: {", ".join(self.hijos)}
        """

nomPadre = input("Ingrese nombre del padre: ")
nomMadre = input("Ingrese nombre de la madre: ")
hijos = []

while True:
    print("Ingrese * si no tiene mas hijos")
    a = input("Ingrese nombre de su hijo >>> ")
    if a != "*":
        hijos.append(a)
    else:
        break

familia = Familia(nomPadre, nomMadre, hijos)
print(familia)