while True:
    try:
        print("Usted va a realizar la division de dos numeros")
        num1 = float(input("Ingrese el primer numero -->  "))
        num2 = float(input("Ingrese el segundo numero -->  "))
        division = num1/num2
        print(division)
    except ValueError:
        print("Solo se pueden ingresar numeros")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    finally:
        cierre = input("Desea continuar (S/N) -->  ")
        if (cierre.lower()=="n"):
            break
