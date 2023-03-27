def contador(frase):

    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    contador = 0

    for caracter in frase:
        if caracter in vocales:
            contador += 1


    return contador

a = input("Ingrese una frase \n >>> ")
print(contador(a))