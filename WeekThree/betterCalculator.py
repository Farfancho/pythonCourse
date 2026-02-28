#!/usr/bin/env python3

def main():
    op = input("enter an operator ( +, -, *, /): ")
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    match op:
        case "+":
            print(f"{n1} + {n2} = {n1+n2}")
        case "-":
            print(f"{n1} - {n2} = {n1-n2}")
        case "*":
            print(f"{n1} * {n2} = {n1*n2}")
        case "/":
            if n2 != 0:
                print(f"{n1} / {n2} = {n1/n2}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operator")

if __name__ == "__main__":
	main()