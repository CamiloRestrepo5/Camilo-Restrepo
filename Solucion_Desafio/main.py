# Desafío condicionales

print("Por favor ingresa las 5 calificaciones que tuviste durante el curso")

calificacion1 = int(input("Ingresa tu calificación: "))
calificacion2 = int(input("Ingresa tu calificación: "))
calificacion3 = int(input("Ingresa tu calificación: "))
calificacion4 = int(input("Ingresa tu calificación: "))
calificacion5 = int(input("Ingresa tu calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3 +
            calificacion4 + calificacion5) / 5

print(f"El total de tu calificación es:{promedio}")

if promedio >= 60:
    print("Aprobaste el curso")
elif promedio >= 40:
    print("Puedes recuperar el curso")
else:
    print("Reprobaste el curso")
