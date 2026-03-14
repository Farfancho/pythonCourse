# Ejercicio: diccionarios
# Tema: información de un estudiante

print("=== Ficha de estudiante con diccionarios ===")

# TODO 1: crea un diccionario con la información de un estudiante
estudiante = {
    "nombre": "Laura",
    "edad": 19,
    "carrera": "Ingeniería"
}

# TODO 2: imprime el diccionario completo
print("Datos del estudiante:")
print(estudiante)

# TODO 3: accede a cada dato por su clave
print("\nNombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])
print("Carrera:", estudiante["carrera"])

# TODO 4: modifica la edad
estudiante["edad"] = 20

# TODO 5: agrega una nueva clave: semestre
estudiante["semestre"] = 4

# TODO 6: imprime el diccionario actualizado
print("\nDiccionario actualizado:")
print(estudiante)

# TODO 7: muestra claves, valores e items
print("\nClaves:", estudiante.keys())
print("Valores:", estudiante.values())
print("Items:", estudiante.items())

# TODO 8: usa get para consultar una clave que no exista
print("\nTeléfono:", estudiante.get("telefono", "No registrado"))