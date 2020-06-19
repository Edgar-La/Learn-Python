#Salary increase program.
#If your salary is lees than 1000, it´ll increase 17%
#otherwise, it´ll increase 12%

#By Edgar Lara
#05-14-2020

import os
os.system("clear")

print("Type our salary: ")
worker_salary = float(input())

#Always is True, assuming the worker type correct salary
flag_data = True
if (worker_salary <= 0):
	print("Oops, something is really bad.")
	#If the wroker type wrong, then it´ll be False
	flag_data = False
#The corresponding calculus
elif (worker_salary < 1000):
	new_worker_salary = worker_salary * 1.17
	percent_rise = 17
else:
	new_worker_salary = worker_salary * 1.12
	percent_rise = 12
#If everything was okay since the begginning, then show salary
if (flag_data != False):	
	print("Your old salary is: " + str(worker_salary))
	print("Your new salary is: " + str(new_worker_salary))
	print("Pay rise of: " + str(percent_rise) + "%")