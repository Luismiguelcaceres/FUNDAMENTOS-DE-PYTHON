temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# apartado de indices (positivos y negativos)
print("Primer día:", temperaturas[0], temperaturas[-14])
print("Último día:", temperaturas[13], temperaturas[-1])
print("Día 7 (mitad):", temperaturas[6], temperaturas[-8])
print("Penúltimo día:", temperaturas[12], temperaturas[-2])


semana1 = temperaturas[0:7]
semana2 = temperaturas[7:14]
dias_pares = temperaturas[1::2]
invertida = temperaturas[::-1]

print("Primera semana:", semana1)
print("Segunda semana:", semana2)
print("Días pares:", dias_pares)
print("Lista invertida:", invertida)

promedio1 = sum(semana1) / len(semana1)
promedio2 = sum(semana2) / len(semana2)

print("Promedio semana 1:", round(promedio1, 2))
print("Promedio semana 2:", round(promedio2, 2))

