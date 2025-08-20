nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su genero (M/F): ")

if (genero == "F" and nombre.lower() < "m") or (genero == "M" and nombre.lower() >= "n"):
    print("Grupo b")
else:
    print("Grupo a") 
