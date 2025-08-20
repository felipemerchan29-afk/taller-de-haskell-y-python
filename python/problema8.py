edad = int(input("Ingrese su edad: "))

if edad < 5:
    precio = 0
elif edad <= 12:
    precio = 10
elif edad <= 17:
    precio = 15
else:
    precio = 20

print("El precio del boleto es: $", precio)
