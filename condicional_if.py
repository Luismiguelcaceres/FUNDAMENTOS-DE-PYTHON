# Ejemplo del if básico
if True:
    print("Se ejecuta la instrucción")

# Ejemplo de estructura if - elif
if False:
    print("condicion 1")
elif False:
    print("condicion 2")
elif True:
    print("condicion 3")
elif True:
    print("condicion 4")


# Ejercicio de clasificación de edad
edad = 20

if edad < 18:
    print("Eres menor de edad")
elif 18 <= edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")


# Estructura condicional anidada
if True:
    if False:
        print("Se ejecuta la instrucción interna 1")
    elif True:
        print("Se ejecuta la instrucción interna 2")
    else:
        print("Se ejecuta el else interno")
else:
    print("No se ejecuta la instrucción principal")
    
    
edad = 80

if edad < 18:
    if edad > 12 and edad < 18:
        print("eres un adolescente")
    else:
        print("eres un nino")        
else:
    if edad >= 18 and edad < 60:
        print("eres adulto")
    else:
        print("eres mayor")
        
# Ejercicio del partido
marcador_colombia = int(input("Ingrese el marcador de Colombia: "))
marcador_chile = int(input("Ingrese el marcador de Chile: "))

if marcador_colombia > marcador_chile:
    print("Colombia es el ganador")
elif marcador_colombia == marcador_chile:
    print("El partido terminó en empate")
else:
    print("Perdió Colombia el partido")
    
# Operador ternario
numero = 4

if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es inpar")
# esto es igual a lo anterior
print("el numero es par" if numero % 2 == 0 else "el numero es inpar")