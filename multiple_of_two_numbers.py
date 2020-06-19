#Given two numbers, verify if one of them is divisible by the other
#By EDgar Lara
#05-16-2020

import os
os.system("clear")

print("Typer first number: ")
number_1 = int(input())
print("Typer second number: ")
number_2 = int(input())

if (number_1%number_2 == 0):
	print("First number is divisible by the second.")
elif (number_2%number_1 == 0):
	print("Second number is divisible by the first.")
else:
	print("Non of them is divisible by the other.")