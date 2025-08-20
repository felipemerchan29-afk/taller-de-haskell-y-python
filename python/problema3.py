try:
    a = float(input("Ingrese el dividendo: "))
    b = float(input("Ingrese el divisor: "))
    resultado = a / b
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
