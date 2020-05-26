#Algorithm to exchange value of 3 variables given by the user
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

print("The actual values for A, B and C are: ")
print(num_A, num_B, num_C)

#The core of the program, the exchange algorithm
num_aux = num_A
num_A = num_B
num_B = num_C
num_C = num_aux

print("The new values for A, B and C are: ")
print(num_A, num_B, num_C)

'''
Basically what we did with the algorithm  is:
B -> A,
C -> B,
A -> C
'''