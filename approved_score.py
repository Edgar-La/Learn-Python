#Program that, given a score obtained in test, check if you approved or not
#By Edgar Lara
#14-05-2020

import os
os.system("clear")

print ("Type your score: ")
score = float(input())

if (score < 0) or (score >10):
	print("Score out of range.")
elif (score >= 8):
	print("You approved the test. Congrats!")
else:
	print ("You failed the test.")