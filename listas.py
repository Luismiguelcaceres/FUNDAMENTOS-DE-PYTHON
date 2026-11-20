lista = ["dato_1", "dato_2", "dato_3"]
print(type(lista))

lista_mixta = ["hola", 123, 3.14, True, ["ADSO", "SST"]]

# LISTA DE APRENDICES SENA 3233140

aprendices = ["miguel", "sebastian", "lixeth", "alejandra"]
print(aprendices)

# ACCEDER A UN ELEMENTO DE LA LISTA
print(aprendices[2]) 

# MODIFICAR UN ELEMENTO DE LA LISTA

aprendices[0] = "luis"
print(aprendices)

# CONSULTAR RANGOS DE ELEMENTOS DENTRO DE LA LISTA

print(aprendices[0:3])
print(aprendices[2:4])
print(aprendices[0::2]) # salto de uno en uno

# CONCATENAR LISTAS

programas_tecnicos = ["sistema teleinformaticos", "tecnico en redes"]
programas_tecnologos = ["adso", "topografia"]

programas_sena = programas_tecnicos + programas_tecnologos
print(programas_sena)

# EXPENDER LISTAS CON EXTEND 

nuevos_programas_tecnicos = ["inteligencia artificial", "mineria de datos", "tecnico en redes"]
programas_tecnicos.extend(nuevos_programas_tecnicos)
print(programas_tecnicos)


print(len(programas_tecnicos))

# ELEMENTOS REPETIDOS DENTRO DE LA LISTA
print(programas_tecnicos)
print(programas_tecnicos.count("tecnico en redes"))

# OBTENER EL ÍNDICE DE UN ELEMENTO 
print(aprendices.index("lixeth"))  
print(programas_tecnicos.index("inteligencia artificial"))
print(programas_tecnologos.index("adso"))

# COPIAR UNA LISTA CON LA FUNCION COPY

nueva_lista_aprendices = aprendices.copy()
print(nueva_lista_aprendices)

#   NUEVOS ELEMENTOS CON  LA FUNCION APPEND()

nueva_lista_aprendices.append("adriana")
print(nueva_lista_aprendices)

#  MUEVO ELEMENTO EN DISTINTO INDICE

nueva_lista_aprendices.insert(1, "camilo")
print(nueva_lista_aprendices)

# ELIMINAR UN ELMENTO  . remove() elimina la primera concidencia 

nueva_lista_aprendices.remove("camilo")
print(nueva_lista_aprendices)

# ELIMINA EL ELEMENTO SEGUN EL INDICE .POP()

nueva_lista_aprendices.pop(0)
print(nueva_lista_aprendices)

# . CLREAR LIMPIA TODOS LOS ELEMTOS DE LS LIOSTA 

# nueva_lista_aprendices.clear()
# print(nueva_lista_aprendices)


# ORDENAR LA LISTA 
# ORDENAR ACENDENTEMENTE A-Z .sort()

nueva_lista_aprendices.sort()
print(nueva_lista_aprendices)

# ORDENAR DECENDENTEMENTE

nueva_lista_aprendices.reverse()
print(nueva_lista_aprendices)

#  BUSCAR ELEMENTOIS EN LA LISTA CON EL OPERADOR IN
if "lixeth" in nueva_lista_aprendices:
    print("lixeth se encontro en la lista de aprendices")
else:
    print("lixeth no se encontro")