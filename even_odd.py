#Programa that given a natural number,
#tells if is even or odd

#By Edgar Lara
#05-14-2020

import os
os.system("clear")

#N: n=0,1,2,3,...
print("Type a natural number")
number = int(input())

def even_odd(num):
	if(num < 0):
		print("You type a non natural number.")
	elif (num%2 == 0):
		print("The number is even.")
	else:
		print("The number is odd.")

even_odd(number)