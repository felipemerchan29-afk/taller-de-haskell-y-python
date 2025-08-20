puntuacion = float(input("Ingrese su puntuación: "))

if puntuacion < 3:
    nivel = "Bajo"
    recompensa = 100
elif puntuacion <= 6:
    nivel = "Medio"
    recompensa = 500
else:
    nivel = "Alto"
    recompensa = 1000
print("Nivel de rendimiento:", nivel)
print("Recompensa: $", recompensa)
