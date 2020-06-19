#This program ask for a year, and tells you if it is past, present or future
#By Edgar Lara
#05-14-2020

import os
os.system("clear")
import datetime

print("Compute a year")
typed_year = int(input())

#Function to always get the actual year
def get_year():
	now = datetime.datetime.now()
	current_year = now.strftime("%Y")
	return (int(current_year))
actual_year = get_year()

def comparison_years(value_year):
	if (value_year < actual_year):
		print("The year you typed is past.")
		print("We are now in " + str(typed_year) + ".")
	elif (value_year == actual_year):
		print("The year you typed is actually the current year.")
	else:
		print("The year you typed is future.")
		print("We are now in " + str(typed_year) + ".")
comparison_years(typed_year)