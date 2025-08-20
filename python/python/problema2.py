contraseña_guardada = "1234"

entrada = input("Ingrese la contraseña: ")

if entrada.lower() == contraseña_guardada.lower():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
