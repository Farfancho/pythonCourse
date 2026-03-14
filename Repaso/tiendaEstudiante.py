##Enunciado

##Desarrolla un programa en Python que simule una tienda universitaria.

##El programa debe pedir el nombre, la edad, el saldo disponible y si el cliente es estudiante. Luego debe mostrar un menú de productos y permitir comprar varios productos usando un ciclo while.

##Por cada compra, el programa debe pedir la opción del producto y la cantidad. Después debe calcular el subtotal, aplicar descuentos según las condiciones dadas y verificar si el usuario tiene suficiente saldo.

##Al final, el programa debe mostrar un resumen completo de la compra.

##Reglas

##estudiante → 10% de descuento

##3 o más unidades del mismo producto → 5% adicional

##si no alcanza el saldo → no se realiza la compra

##si elige 0 → sale del programa


print("=== Tienda universitaria ===")

# -----------------------------------
# 1. Registro del cliente
# -----------------------------------
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
saldo = float(input("Ingrese su saldo disponible: "))
respuesta_estudiante = input("¿Es estudiante? (si/no): ").lower()

es_estudiante = respuesta_estudiante == "si"

# -----------------------------------
# 2. Variables acumuladoras
# -----------------------------------
total_gastado = 0
total_productos = 0
numero_compras = 0

# -----------------------------------
# 3. Ciclo principal
# -----------------------------------
while saldo > 0:
    print("\n--- Menú de productos ---")
    print("1. Cuaderno    - $8500")
    print("2. Lápiz       - $1200")
    print("3. Calculadora - $25000")
    print("4. USB         - $18000")
    print("0. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 0:
        print("Saliendo de la tienda...")
        break

    elif opcion < 0 or opcion > 4:
        print("Opción no válida.")
        continue

    cantidad = int(input("Ingrese la cantidad: "))

    if cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
        continue

    # -----------------------------------
    # 4. Determinar precio según opción
    # -----------------------------------
    if opcion == 1:
        producto = "Cuaderno"
        precio = 8500
    elif opcion == 2:
        producto = "Lápiz"
        precio = 1200
    elif opcion == 3:
        producto = "Calculadora"
        precio = 25000
    else:
        producto = "USB"
        precio = 18000

    # Mensaje especial
    if edad < 16 and opcion == 3:
        print("Consulta con tu docente si realmente necesitas este producto.")

    # -----------------------------------
    # 5. Cálculos
    # -----------------------------------
    subtotal = precio * cantidad
    descuento = 0

    if es_estudiante:
        descuento += subtotal * 0.10

    if cantidad >= 3:
        descuento += subtotal * 0.05

    total_compra = subtotal - descuento

    print(f"\nProducto: {producto}")
    print(f"Subtotal: ${subtotal}")
    print(f"Descuento: ${descuento}")
    print(f"Total a pagar: ${total_compra}")

    # -----------------------------------
    # 6. Validar saldo
    # -----------------------------------
    if total_compra > saldo:
        print("No tiene saldo suficiente para realizar esta compra.")
    else:
        saldo -= total_compra
        total_gastado += total_compra
        total_productos += cantidad
        numero_compras += 1

        print("Compra realizada con éxito.")
        print(f"Saldo restante: ${saldo}")

# -----------------------------------
# 7. Resumen final
# -----------------------------------
print("\n=== Resumen final ===")
print(f"Cliente: {nombre}")
print(f"Saldo restante: ${saldo}")
print(f"Total gastado: ${total_gastado}")
print(f"Total de productos comprados: {total_productos}")
print(f"Número de compras realizadas: {numero_compras}")

if total_gastado > 50000:
    print("Gracias por tu compra grande.")
elif numero_compras == 0:
    print("No realizaste ninguna compra.")
else:
    print("Gracias por tu compra.")