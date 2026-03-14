# Ejercicio: tuplas
# Tema: coordenadas en el plano

print("=== Coordenadas con tuplas ===")

# TODO 1: crea una tupla con las coordenadas de un punto
punto = (3, 7)

# TODO 2: imprime la tupla completa
print("Punto:", punto)

# TODO 3: imprime x e y por separado usando índices
print("Coordenada x:", punto[0])
print("Coordenada y:", punto[1])

# TODO 4: desempaqueta la tupla en dos variables
x, y = punto
print("\nDesempaquetado:")
print("x =", x)
print("y =", y)

# TODO 5: calcula la distancia al origen
distancia = (x**2 + y**2) ** 0.5
print("Distancia al origen:", distancia)

# TODO 6: intenta pensar por qué una tupla tiene sentido aquí
print("\nReflexión:")
print("La coordenada se guarda como tupla porque representa un dato fijo y ordenado.")