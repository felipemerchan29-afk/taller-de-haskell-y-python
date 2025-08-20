edad = int(input("Ingrese su edad: "))
ingreso = float(input("Ingrese sus ingresos mensuales: "))

if edad >= 18 and ingreso >= 53206000:
    print("Debe pagar impuestos")
else:
    print("No necesita pagar impuestos")
