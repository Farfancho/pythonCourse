#!/usr/bin/env python3

def main():
    op = input("Enter the operation you want to perform (Cm to m, m to Cm, m to Km, Km to m): ")
    x  = float(input("Enter the value you want to convert: "))
    match op:
        case "Cm to m":
            print(f"{x} cm is {x/100} m")
        case "m to Cm":
            print(f"{x} m is {x*100} cm")
        case "m to Km":
            print(f"{x} m is {x/1000} km")
        case "Km to m":
            print(f"{x} km is {x*1000} m")
        case _:
            print("Invalid operation")
            
if __name__ == "__main__":
	main()