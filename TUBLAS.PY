#TUPLAS

#ESTRUCTURA DE UNA TUPLA 

#INDICE      0               1            2
tupla = ("elemento_1", "elemento_2", "elemento_3")
print(type(tupla))  #Class Tuple

tupla_2 = "a", "b", "c"
print(type(tupla_2))   #Class Tuple

tupla_3 = ("Hola",)
print(type(tupla_3))   #Class Tuple

tupla_4 = ("Hola")
print(tupla_4)  #(H, o, 1, a)
print(type(tupla_4))  #Class STR

tupla_mixta = ("Hola", 123, 3.14, True,[])
print(type(tupla_mixta))

#TUPLAS DE APRENDICES SENA ADSO 3233140

aprendices = ("Dayana", "Jhon", "Oscar", "Miguel", "Pepito", "Jhon")
print(aprendices)

#ACCEDER A UN ELEMENTO DE LA TUPLA 

print(aprendices[2])

#MODIFICAR UN ELEMENTO DE LA LISTA

#aprendices[0] = "Diana"
#print(aprendices)  #esto genera un error porque las tuplas no son modificables 

#CONSULTAR RANGO DE ELEMENTOS EN LAS TUPLAS 
print(aprendices[0:2])
print(aprendices[1:4])  #('Jhon', 'Oscar', 'Miguel')
print(aprendices[1:])   #('Jhon', 'Oscar', 'Miguel', 'Pepito')

#CONCATENAR TUPLAS+

tupla_uno = (1,2,3)
tupla_dos = (4,5,6)

tupla_suma = tupla_uno + tupla_dos
print(tupla_suma)

#MULTIPLICAR UNA TUPLA 

tupla_multiplicada = tupla_suma*3
print(tupla_suma)

#METODOS DE LAS TUPLAS--------------

#MEDIR LA LONGITUD DE UNA TUPLA .len()

print(len(aprendices))

#MEDIR LA LONGITUD DE UNA TUPLA .count()

print(aprendices.count("Jhon"))  #SE ENCUENTRA REPETIDO 2 VECES 

#OBTENER EL INDICE DE UN ELEMENTO .index()

print(aprendices.index("Dayana"))  #SE ENCUENTRA EN EL INDICE 0 

#MODIFICAR UNA TUPLA CONVIRTIENDOLA EN UNA LISTA

lenguajes = ("HTML", "CSS", "JAVA", "PYTHON")
print(type(lenguajes))  #<class 'tuple'>

lista_lenguajes = list(lenguajes) #SE HACE CASTEO 
print(lista_lenguajes)
print(type(lista_lenguajes)) #<class 'list'>

lista_lenguajes.append("PYTHON")  #PODEMOS AGREGAR UN ELEMENTO 
print(lista_lenguajes)  #['HTML', 'CSS', 'JAVA', 'PYTHON', 'PYTHON']

lenguajes = tuple(lista_lenguajes) #PODEMOS DEVOLVER NUEVAMENTE A TUPLA
print(type(lenguajes))  #<class 'tuple'>

#COMPROBACION DE PERTENENCIA CON "IN" busqueda

print("PYTHON" in lenguajes) #TRUE
print("C++" in lenguajes)    #FALSE

if "HTML" in lenguajes:
    print("HTML fue encontrado en tu busqueda")
else: 
    print("HTML no fue encontrado en tu busqueda")
    
#EMPAQUETAR TUPLAS

programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "TOPOGRAFIA"

tupla_programas = (programa_1, programa_2, programa_3)
print(tupla_programas)  # SE EMPAQUETAN EN UN SOLA VARIABLE ('ADSO', 'SST', 'TOPOGRAFIA')
print(type(tupla_programas))  #<class 'tuple'>

#DESEMPAQUETAR TUPLAS

tupla_ciudades = ("Duitama", "Sogamoso", "Tunja")

ciudad_1, ciudad_2, ciudad_3 = tupla_ciudades  #DESEMPAQUETAR LAS CIUDADES

print(ciudad_1)  #DUITAMA
print(ciudad_2)  #SOGAMOSO
print(ciudad_3)  #TUNJA

#ITERAR O RECORRER UNA TUPLA "FOR"

for ciudad in tupla_ciudades:
    print(tupla_ciudades)  #('Duitama', 'Sogamoso', 'Tunja')