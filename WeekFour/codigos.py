# Ejercicio: sets
# Tema: códigos de estudiantes sin repetir

print("=== Códigos únicos con sets ===")

# TODO 1: crea una lista con códigos repetidos
codigos = [101, 102, 101, 103, 104, 102, 105]

# TODO 2: conviértela en set
codigos_unicos = set(codigos)

# TODO 3: muestra el set resultante
print("Códigos únicos:", codigos_unicos)

# TODO 4: agrega un nuevo código
codigos_unicos.add(106)
print("Después de agregar 106:", codigos_unicos)

# TODO 5: elimina un código
codigos_unicos.remove(102)
print("Después de eliminar 102:", codigos_unicos)

# TODO 6: verifica si cierto código pertenece al set
print("¿Está 103?", 103 in codigos_unicos)
print("¿Está 200?", 200 in codigos_unicos)

# TODO 7: crea otro set y halla la intersección
grupo_b = {103, 104, 200, 300}
comunes = codigos_unicos & grupo_b

print("Grupo B:", grupo_b)
print("Códigos en común:", comunes)