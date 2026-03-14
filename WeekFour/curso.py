# Ejercicio integrador: usar las 4 estructuras

print("=== Sistema básico de estudiante ===")

# Lista: notas
notas = [4.2, 3.8, 4.5]

# Tupla: salón (bloque, aula)
salon = ("Edificio A", 204)

# Diccionario: datos del estudiante
estudiante = {
    "nombre": "Carlos",
    "edad": 20,
    "carrera": "Ingeniería"
}

# Set: materias inscritas
materias = {"Python", "Cálculo", "Física", "Python"}

print("\n--- Datos iniciales ---")
print("Notas:", notas)
print("Salón:", salon)
print("Estudiante:", estudiante)
print("Materias:", materias)

# TODO 1: agrega una nueva nota
notas.append(4.7)

# TODO 2: calcula el promedio
promedio = sum(notas) / len(notas)

# TODO 3: agrega el semestre al diccionario
estudiante["semestre"] = 3

# TODO 4: agrega una nueva materia al set
materias.add("Álgebra")

print("\n--- Datos actualizados ---")
print("Notas:", notas)
print("Promedio:", promedio)
print("Salón:", salon)
print("Estudiante:", estudiante)
print("Materias:", materias)