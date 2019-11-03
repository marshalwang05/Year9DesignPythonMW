import math

def calcVolumeCylinder(radius, height):
	if radius>=0 and height>=0:
		volume = math.pi * pow(radius,2) * height
		volume = round(volume,2)
		return volume
	else:
		return -1

print("Start Program")
result = calcVolumeCylinder(-3,4)
print(result)
print("End Program") 