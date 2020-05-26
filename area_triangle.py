#Program that calculate the area of a triangle
#By Edgar Lara
#14-05-2020


#This is for clear the window of the console
import os
os.system("clear")

#Compute the data of variables
print("Compute the magnithe of base of triangle: ")
base_triangle = float(input())
print("Compute the magnithe of height of triangle: ")
height_triangle = float(input())

#Function to calculate area
def area_triangle(basetriangle, heighttriangle):
	return ((basetriangle * heighttriangle) / 2)

#print the result
area = area_triangle(base_triangle, height_triangle)
print("\nThe area of the triangle is " + str(round(area,4)))

'''Or even a little bit more simpler, you can skip the
   of funcionts:

area=((base_triangle * height_triangle) / 2)

print(area)'''