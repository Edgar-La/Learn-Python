import os
os.system("clear")

#We need to start the variables with values.
#It wont afect the total bill.
loop = True
total_bill=0.0

#Verify only positive integers quantity items
def items_value():
	value = int(input())
	while (value < 0):
		print("Only positive integers: ")
		value = int(input())
	return value
#Verify onlu positive prices
def items_price():
	PRICE = float(input())
	while (PRICE < 0):
		print("No negative prices: ")
		PRICE = int(input())
	return PRICE
#Calculate the bill
def function_bill(num1, num2, num3):
	num1 =  num1 + (num2 * num3)
	return num1



while (loop == True):
	print("Number of items: ")
	cant = items_value()
	if (cant == 0):
		break
	print("Unitary price: ")
	item_price = items_price()
	total_bill = function_bill(total_bill, cant, item_price)
	
print("The total bill is: $" + str(total_bill))

