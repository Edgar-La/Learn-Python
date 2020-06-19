#Given 3 numbers, show the Min and Max
#Then, print the 3 in ascendent order

#By Edgar Lara
#05-14-2020

import os
os.system("clear")

#Compute the requiere values
print("Type the value of A: ")
num_A = float(input())
print("Type the value of B: ")
num_B = float(input())
print("Type the value of C: ")
num_C = float(input())
##########################################
def max_num(A,B,C):
	if (A > B):
		if(A > C):
			print("Max = A = " + str(A))
		else:
			print("Max = C = " + str(C))
	elif (B > C):
		print("Max = B = " + str(B))
	else:
		print("Max = C = " + str(C))
##########################################
def min_num(A,B,C):
	if (A < B):
		if(A < C):
			print("Min = A = " + str(A))
		else:
			print("Min = C = " + str(C))
	elif (B < C):
		print("Min = B = " + str(B))
	else:
		print("Min = C = " + str(C))
##########################################
def order_nums(A, B, C):
	if (A < B):
		if(A < C):
			if (B < C):
				print(A,B,C)
			else:
				print(A,C,B)
		else:
			print(C,A,B)
	else:
		if (B < C):
			if (A < C):
				print(B,A,C)
			else:
				print(B,C,A)
		else:
			print(C,B,A)
##########################################
max_num(num_A, num_B, num_C)
min_num(num_A, num_B, num_C)
print("The numbers in ascendent order: ")
order_nums(num_A, num_B, num_C)