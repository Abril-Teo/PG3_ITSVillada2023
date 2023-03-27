def comprobar(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

año = int(input("Ingrese un año \n >>> "))

if comprobar(año):
    print(año, "año bisiesto.")
else:
    print(año, "no es año bisiesto.")
