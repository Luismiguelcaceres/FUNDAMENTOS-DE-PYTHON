# Operadores de asignación

x = 5
print("Valor inicial:", x)

# Asignación con suma (+=)
x += 2  # Es lo mismo que: x = x + 2
print(x)

# Asignación con multiplicación (*=)
x *= 2  # Es lo mismo que: x = x * 2
print(x)

# Asignación con resta (-=)
x -= 2  # Es lo mismo que: x = x - 2
print("Resta:", x)

# Asignación con división (/=)
x /= 2  # Es lo mismo que: x = x / 2
print(x)


# Ejercicio: producto con descuento

precio = 100000
descuento = 0.2

print("Precio original:", precio)

precio_final = precio - (precio * descuento)
print(precio_final)


# Operador Walrus (Python 3.8 o superior)
# Permite asignar un valor a una variable y evaluarla/imprimirla en la misma línea
print(z := 10)