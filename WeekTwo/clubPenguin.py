#!/usr/bin/env python3

def main():
    age = int(input("Enter your age: "))
    if age < 0:
        print("Age cannot be negative")
    elif 0 <= age <= 8:
        print("You are a minor")
    elif 9 <= age <= 12:
        print("You are a teenager")
    elif 13 <= age <= 17:
        print("You are a bigger teenager")
    elif age >= 18:
        print("You are just old")

if __name__ == "__main__":
	main()