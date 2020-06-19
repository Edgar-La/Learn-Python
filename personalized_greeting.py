'''Personalized greeting
 8 <= h < 13 -> Good morning
13 <= h < 15 -> Enjoy the food
15 <= h < 17 -> Coffee hour
17 <= h < 20 -> Dinner time
otherwise -> Good night'''

#By Edgar Lara
#05-14-2020

import os
os.system("clear")

#We call the module of current time
import datetime

'''	We use the module to get current time, and then save the time in string
	We save only the hourr of string into int'''
def time_now ():
	current_time = datetime.datetime.now()
	print (current_time.strftime("%H:%M:%S"))
	hour_time_str = current_time.strftime("%H:%M:%S")
	return (int(hour_time_str[0:2]))
hour_time_int = time_now()

#According to hour we display the greeting
def greeting(h):
	if (8 <= h < 13):
		print("Good morning")
	elif (13 <= h < 15):
		print("Enjoy the food")
	elif (15 <= h < 17):
		print("Coffee hour")
	elif (17 <= h < 20):
		print("Dinner time")
	else:
		print("Good night")
greeting(hour_time_int)