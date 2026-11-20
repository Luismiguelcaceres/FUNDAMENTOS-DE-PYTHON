peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

if peso > 0 and estatura > 0:
    imc = round(peso / (estatura ** 2), 2)

    if imc < 18.5:
        clasificacion = "bajo peso"
    elif imc < 25:
        clasificacion = "normal"
    elif imc < 30:
        clasificacion = "sobrepeso"
    else:
        clasificacion = "obesidad"

    print(f"Su imc es: {imc}")
    print(f"Clasificación: {clasificacion}")
else:
    print("Error: el peso y la estatura deben ser valores positivos")
    