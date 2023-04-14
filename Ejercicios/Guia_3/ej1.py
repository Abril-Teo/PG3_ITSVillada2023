while True:
    try:
        print("Usted va a realizar la suma de dos numeros")
        num1 = float(input("Ingrese el primer numero -->  "))
        num2 = float(input("Ingrese el segundo numero -->  "))
        suma = num1+num2
        print(suma)
    except ValueError:
        print("Solo se pueden ingresar numeros")
    finally:
        cierre = input("Desea continuar (S/N) -->  ")
        if (cierre.lower()=="n"):
            break
