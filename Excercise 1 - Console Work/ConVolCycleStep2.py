import math


name = input("What is your name: ")
r=input("Input radius (cm): ")
r=int(r)
h=input("Input height (cm): ")
h=int(h)


print("Hi "+name+"!")
print("In a cylinder with:")
print("Radius = "+str(r))
print("Height = "+str(h))

V=(math.pi)*r*r*h
V=round(V,2)

print("The volume of the cylinder is ",V)