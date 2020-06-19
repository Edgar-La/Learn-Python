import os

check = True
os.system("clear")

print("What operation do you want to do:")
print("1) Addition, 2)Subtraction, 3)Multiplication, 4)Division")
option = int(input())


print("Type the first number")
number_1 = float(input())
print("Type the second number")
number_2 = float(input())
while (number_2 == 0):
	print("No division by cero, type second number again: ")
	number_2 = float(input())
	

def Addition(num1, num2):
	return(num1+num2)
def Subtraction(num1, num2):
	return(num1-num2)
def Multiplication(num1, num2):
	return(num1*num2)
def Division(num1, num2):
	return(num1/num2)

def select_oper (i):
	operation = {
	1 : Addition(number_1, number_2),
	2 : Subtraction(number_1, number_2),
	3 : Multiplication(number_1, number_2),
	4 : Division(number_1, number_2)
	}
	return(operation.get(i))

n = select_oper(option)
print("\nThe result of the operation is: " + str(n))