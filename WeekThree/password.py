#!/usr/bin/env python3

def main():
    clave_ok = "python123"
 
    clave = input("Contraseña: ")
    while clave != clave_ok:
     print("Incorrecta, intente de nuevo")
     clave = input("Contraseña: ")
 
    print("Acceso")

if __name__ == "__main__":
	main()