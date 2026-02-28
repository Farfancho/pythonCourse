#!/usr/bin/env python3

def main():
    clave_ok = "python123"
 
    while True:
     clave = input("Contraseña: ")
     if clave == clave_ok:
      print("Acceso")
      break
     else:
      print("Incorrecta, intente de nuevo")

if __name__ == "__main__":
	main()