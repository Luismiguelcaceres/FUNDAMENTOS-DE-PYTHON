canciones = ["Low key", "Hoy cobre", "No renotorno", "Back and yellow", "Sweet Child O Mine"]
print("Lista inicial:", canciones)

canciones.append("Low key")
print("Después de append:", canciones)


canciones.insert(1, "black and yellow")
print("Después de insert:", canciones)


canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print("Después de extend:", canciones)

canciones.remove("No retorno")
print("despues de remove:", canciones)


eliminada = canciones.pop()
print("cancion eliminada con pop:", eliminada)
print("despues de pop:", canciones)


canciones.sort()
print("Lista ordenada:", canciones)

print("cantidad de canciones:", len(canciones))
print("posición de Low key:", canciones.index("Low key"))
print("veces que aparece Bonus Track 1:", canciones.count("Bonus Track 1"))