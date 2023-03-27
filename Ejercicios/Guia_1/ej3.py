ancho = int(input("Ingrese el ancho \n >>> "))
alto = int(input("Ingrese el alto \n >>> "))
caracter = input("Ingrese el caracter \n >>> ")

for i in range(alto):
    for j in range(ancho):
        print(caracter, end="")
    print()