# Actividad 2: Calculadora de Notas
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = round((nota1 + nota2 + nota3) / 3, 2)
nota_maxima = 5.0
puntos_faltantes = round(nota_maxima - promedio, 2)


if promedio >= 3.0:
    print("APROBO")
else:
    print("reprobado") 

print("resultado de las notas")
print(f"notas ingresadas: {nota1}, {nota2}, {nota3}")
print(f"Promedio final: {promedio}")
print(f"Puntos que le faltan para la nota maxima (5.0): {puntos_faltantes}")
print(f"el aprendiz aprueba?: {aprueba}")