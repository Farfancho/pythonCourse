#!/usr/bin/env python3

def main():
    palabra = input("Enter a word: ")
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    print(f"The number of vowels in the word is: {contador}")  
            
if __name__ == "__main__":
	main()