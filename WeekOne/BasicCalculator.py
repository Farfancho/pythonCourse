#!/usr/bin/env python3

def main():
	num1 = int(input("Enter the first number: "))
	num2 = int(input("Enter the second number: "))
	print(f"The sum of {num1} and {num2} is {num1 + num2}")
	print(f"The difference of {num1} and {num2} is {num1 - num2}")
	print(f"The product of {num1} and {num2} is {num1 * num2}")
	if num2 != 0:
		print(f"The quotient of {num1} and {num2} is {num1 / num2}")
	else:
		print("Cannot divide by zero")

if __name__ == "__main__":
	main()
