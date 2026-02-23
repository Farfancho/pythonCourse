#!/usr/bin/env python3

def main():
    firstGrade = int(input("Enter the first grade: "))
    secondGrade = int(input("Enter the second grade: "))
    thirdGrade = int(input("Enter the third grade: "))
    average = (firstGrade + secondGrade + thirdGrade) / 3
    print(f"The average of {firstGrade}, {secondGrade}, and {thirdGrade} is {average}")

if __name__ == "__main__":
	main()