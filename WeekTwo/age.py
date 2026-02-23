#!/usr/bin/env python3

def main():
    currentYear = int(input("Enter the current year: "))
    birthYear = int(input("Enter your birth year: "))
    Age = currentYear - birthYear
    print(f"Your age is {Age}")

if __name__ == "__main__":
	main()