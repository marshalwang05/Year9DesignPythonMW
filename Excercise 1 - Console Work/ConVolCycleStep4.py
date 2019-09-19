import math

print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03C0\u00d7radius\u00b2\u00d7height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")

file = open("data.txt","a")

name = input("\n\tWhat is your name: ")

r=1
h=1

while (r!=0 or h!=0):

	try:
		r=input("\n\tInput radius (cm): ")
		r=int(r)
		h=input("\n\tInput height (cm): ")
		h=int(h)
	except:
		print("\n\t\tEnter a numeric value")
		h=-1
		r=-1

	if (r>=0 or h>=0):

		V=(math.pi)*r*r*h
		V=round(V,2)
		print("\n\t\tHi "+name+"!")
		print("\n\t\tIn a cylinder with:")
		print("\n\t\tRadius = "+str(r))
		print("\n\t\tHeight = "+str(h))
		file.write(str(V)+"\n")

		print("\n\tThe volume of the cylinder is ",V)
	else:
		print("\n\t\tYou have entered an invalid value")

print("END PROGRAM")
file.close()