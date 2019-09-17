import math

print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03C0\u00d7radius\u00b2\u00d7height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")

name = input("\n\tWhat is your name: ")
r=input("\n\tInput radius (cm): ")
r=int(r)
h=input("\n\tInput height (cm): ")
h=int(h)


print("\n\tHi "+name+"!")
print("\n\tIn a cylinder with:")
print("\n\tRadius = "+str(r))
print("\n\tHeight = "+str(h))

V=(math.pi)*r*r*h
V=round(V,2)

print("\n\tThe volume of the cylinder is ",V)