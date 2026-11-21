#DICICIONARIOS

#ESTRUCTURA DE UN DICICONARIO

diccionario = {
    "clave_1": "valor_1",
    "clave_2": "valor_2",
    "clave_3": "valor_3",
}

#DICCIONARIO VACIO 

diccionario_vacio = {}
print(type(diccionario_vacio))  #<class 'dict'>

#DICCIONARIO CON ELEMENTOS 

diccionario_aprendiz = {
    "nombre": "Lizeth",
    "apellido": "Garcia",    
    "programa": "ADSO",
    "ficha": "3233140",
    "edad": 25
}
print(diccionario_aprendiz)

#OBTENER UN VALOR DEL DICCIONARIO

print(diccionario_aprendiz["programa"])  #ADSO
#print(diccionario_aprendiz["correo"])    #KEY ERROR

print(diccionario_aprendiz.get("programa"))
print(diccionario_aprendiz.get("correo"))

#OBTENER SOLO LAS CLAVES DEL DICCIONARIO .keys()

print(diccionario_aprendiz.keys())
#dict_keys(['nombre', 'apellido', 'programa', 'ficha', 'edad'])

#OBTENER SOLO LOS VALORES DEL DICCIONARIO .values()

print(diccionario_aprendiz.values())
#dict_values(['Lizeth', 'Garcia', 'ADSO', '3233140', 25])

#OBTENER LA CLAVE Y EL VALOR DEL DICCIONARIO .items()

print(diccionario_aprendiz.items())
#dict_items([('nombre', 'Lizeth'), ('apellido', 'Garcia'), ('programa', 'ADSO'), ('ficha', '3233140'), ('edad', 25)])

#AGREGAR O CREAR UN NUEVO ELEMENTO AL DICCIONARIO

diccionario_aprendiz["correo"] = "mlgf5832@gmail.com"
print(diccionario_aprendiz)

#MODIFICAR UN VALOR DEL DICCIONARIO

diccionario_aprendiz["programa"] = "SST"
print(diccionario_aprendiz)

#METODO UPDATE() PARA ACTUALIZAR UN VALOR 

diccionario_aprendiz.update({"nombre": " Maria"})
print(diccionario_aprendiz)

#AGREGAR UN NUEVO ELEMENTO CON UPDATE()

diccionario_aprendiz.update({"ciudad": "Duitama"})
print(diccionario_aprendiz)

#ELIMINAR UN ELEMENTO DEL DICCIONARIO 

#PERMITE ELIMINAR EL ULTIMO ELEMENTO AGREGADO CON .popitem()

diccionario_aprendiz.popitem()
print(diccionario_aprendiz)

#ELIMINAR UN ELEMENTO ESPECIFICO .pop()

diccionario_aprendiz.pop("edad")
print(diccionario_aprendiz)

#ELIMINAR TODOS LOS ELEMENTOS CON .CLEAR()
#diccionario_aprendiz.clear
#print(diccionario_aprendiz)

#COMPROBAR LA PERTENENCIA DE UNA BUSQUEDA CON "IN" 

print("ficha" in diccionario_aprendiz) #TRUE
print("telefono" in diccionario_aprendiz) #FALSE 

if "ficha" in diccionario_aprendiz:
    print("La clave ficha esta dentro del diccionario")  #La clave ficha esta dentro del diccionario
else: 
    print("La clave ficha no esta dentro del diccionario")

#RECORRER UN DICCIONARIO CON EL CICLO "FOR"

# 1. RECORRER SOLO LAS CLAVES DEL DICCIONARIO

for clave in diccionario_aprendiz.keys():
    print(clave)
    
# 2. RECORRER SOLO LOS VALORES DEL DICCIONARIO

for valor in diccionario_aprendiz.values():
    print(valor)
    
# 3. RECORRER TODAS LAS CLAVES Y VALORES DEL DICCIONARIO 

for clave, valor in diccionario_aprendiz.items():
    print(f"{clave} : {valor}")
    
#DICCIONARIOS ANIDADOS ------------

aprendices = {
    "aprendiz_1": {
        "nombre": " James",
        "apellido": "Rodriguez",
        "programa": "ADSO"
    },
    "aprendiz_2": {
        "nombre": " Paula",
        "apellido": "Rodriguez",
        "programa": "SST"
    },
    "aprendiz_3": {
        "nombre": " Pepito",
        "apellido": "Rodriguez",
        "programa": "Minas"
    },
}

#ACCEDER A UN VALOR DE UN DICCIONARIO ANIDADO

print(aprendices["aprendiz_2"]["programa"])  #SST

#RECORRER UN DICCIONARIO CON CICLO "FOR"

for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}:")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")
