print("hello world")

# TIPOS DE ESCRITURA DE VARIABLES EN PYTHON

# CAMELCASE
aprendizSena = "luis"

# PASCALCASE
AprendizSena = "juanes"

# SNAKECASE
aprendiz_sena = "maria"


# TIPOS DE DATOS

# String (str)
nombre = "Luismiguel"
print(type(nombre))

# Integer (int)
edad = 20
print(type(edad))

# Float (float)
altura = 1.77
print(type(altura))

# Boolean (bool)
activo = True
print(type(activo))

# Complex (complex)
complejo = 2 + 3j
print(type(complejo))

# Bytes (bytes)
byte = b"hola"
print(type(byte))

# NoneType
nulo = None
print(type(nulo))


# TIPOS DE DATOS ESTRUCTURADOS

# Lista (list)
lista = ["python", "java", "c++"]
print(type(lista))

# Conjunto (set)
conjunto = {"html", "css"}
print(type(conjunto))

# Tupla (tuple)
tupla = ("python", "java", "c++")
print(type(tupla))

# Diccionario (dict)
diccionario = {"nombre": "luis", "edad": 20}
print(type(diccionario))


# CONVERSION DE TIPOS DE DATOS (CASTING)

telefono = "3242933913"
print(type(telefono))

# Convertir de int a str
telefono_str = str(telefono)
print(type(telefono_str))

cedula = "123456789"
print(type(cedula), cedula)


# CASTING BOOLEANO A ENTERO

matriculado = True
print(type(matriculado))

matriculado_int = int(matriculado)
print(type(matriculado_int), matriculado_int)


# CASTING DECIMAL A ENTERO

promedio = 4.13
print(type(promedio), promedio)

promedio_int = int(promedio)
print(type(promedio_int), promedio_int)


# CASTING ENTERO A DECIMAL

edad = 20
print(type(edad), edad)

edad_float = float(edad)
print(type(edad_float), edad_float)


# CASTING DE ENTERO A BOOLEANO

activo = 0
print(type(activo))

activo_bool = bool(activo)
print(type(activo_bool), activo_bool)


# CASTING DE DECIMAL A BOOLEANO

descuento = 10.5
print(type(descuento), descuento)

descuento_bool = bool(descuento)
print(type(descuento_bool), descuento_bool)


# IDENTACION EN PYTHON

if 5 > 2:
    print("5 es mayor que 2")


# ENTRADA Y SALIDA DE DATOS

# INPUT: Entrada de datos

nombre_completo = input("Ingrese su nombre completo: ")
programa = input("¿Cuál es su programa de formación?: ")


# OUTPUT: Salida de datos

# IMPRESION UTILIZANDO CONCATENACION
print("Hola " + nombre_completo + ", bienvenido al curso de Python")

# IMPRESION UTILIZANDO COMAS
print("Hola", nombre_completo, "bienvenido al curso de Python")

# IMPRESION UTILIZANDO COMAS Y VARIABLES
print(
    "Hola, mi nombre es:",
    nombre_completo,
    "y estoy en el programa de:",
    programa,
)

# IMPRESION CON FORMATO F-STRING
print(
    f"Hola, mi nombre es {nombre_completo} "
    f"y estoy en el programa de: {programa}")