print("Quiere una pizza vegetariana? (si/no)")
respuesta = input().lower()

if respuesta == "si":
    print("Ingredientes disponibles: 1)Piña 2) Champiñones")
    opcion = input("Elija un ingrediente: ")
    ingrediente = "Piña" if opcion == "1" else "Champiñones"
    print("Pizza vegetariana con queso, tomate y", ingrediente)
else:
    print("Ingredientes disponibles: 1) Pepperoni 2) Jamon 3) carnes")
    opcion = input("Elija un ingrediente: ")
    ingredientes = {"1": "Pepperoni", "2": "Jamon", "3": "carnes"}
    ingrediente = ingredientes.get(opcion, "Pepperoni")
    print("Pizza de", ingrediente)
