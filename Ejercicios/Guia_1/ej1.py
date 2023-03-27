def buscar(list, numero):
    try:
        indice = list.index(numero)
        return indice
    except ValueError:
        return -1

# Ejemplo de uso
list = [8,12,9,45]
numero = int(input("Ingrese un número \n >>> "))

indice = buscar(list, numero)
if indice != -1:
    print(f"El elemento {numero} se encuentra en el índice {indice} de la lista.")
else:
    print(f"El elemento {numero} no se encuentra en la lista.")