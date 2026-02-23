#!/usr/bin/env python3

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))  
    boolean = num1 > num2
    print(f"Is {num1} greater than {num2}? {boolean}")

if __name__ == "__main__":
	main()