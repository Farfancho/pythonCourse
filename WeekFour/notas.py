# Ejercicio: listas
# Tema: registro de notas de un estudiante

print("=== Registro de notas con listas ===")

# TODO 1: crea una lista vacía llamada notas
notas = []

# TODO 2: pide al usuario 4 notas y agrégalas a la lista
for i in range(4):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

# TODO 3: imprime la lista completa
print("\nLista de notas:", notas)

# TODO 4: imprime la primera y la última nota
print("Primera nota:", notas[0])
print("Última nota:", notas[-1])

# TODO 5: calcula el promedio
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)

# TODO 6: agrega una nota de recuperación
recuperacion = float(input("\nIngrese la nota de recuperación: "))
notas.append(recuperacion)

# TODO 7: muestra la lista actualizada
print("Lista actualizada:", notas)

# TODO 8: muestra la nota más alta y la más baja
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))