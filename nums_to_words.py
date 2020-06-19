'''Given an integer number, check if it is the range [1,10]
If thats correct, print it with words
If it´s not, print out of range.
'''

#By Edgar Lara
#05-14-2020

import os
os.system("clear") #For clear te screen

#Define a function
#This function is going to map a dictionary
#Dictionary: very usefull tool, one-to-one key-value
def numbers(i):
	switcher = {
	1 : "one",
	2 : "two",
	3 : "tree",
	4 : "four",
	5 : "five",
	6 : "six",
	7 : "seven",
	8 : "eight",
	9 : "nine",
	10 : "ten",
	}
	return switcher.get(i)

#Ask for type a num
print("Type an integer number in the range [1,10]")
num = int(input())

#Check the corresponding tasks
if (num < 1) or (num > 10):
	print("Your number is out of the range [1,10]")
else:
	word_num=numbers(num)
	print("The number " + str(num) + " in words is " + word_num)