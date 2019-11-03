import math
import tkinter as tk

def calcVolumeCylinder(radius, height):
	if radius>=0 and height>=0:
		volume = math.pi * pow(radius,2) * height
		volume = round(volume,2)
		return volume
	else:
		return -1

def runMe():
	print("RUNNING")
	r = RadiusInput.get()
	r = float(r)

	try:
		r=float(r)
		
	except:
		r=-1

	RadiusInput.delete(0,tk.END)
	h = HeightInput.get()
	h = float(h)

	try:
		h=float(h)
	except:
		h=-1

	HeightInput.delete(0,tk.END)

	volume = calcVolumeCylinder(r,h)

	if volume!= -1:
		output.config(state = "normal")
		output.delete("1.0", tk.END)

		result = "\n\n\tr\t= "+str(r)+" units\n\th\t= "+str(h)+" units\n\tvolume\t= "+str(volume)+" units\u00B3"
		output.insert(tk.END, result)
		output.config(state = "disabled")



root = tk.Tk()

title = tk.Label(root, text = "Cylinder Volume Calculator")
title.config(fg = "white", bg = "black")
title.pack(fill = tk.BOTH)

RadiusLabel = tk.Label(root, text = "Radius: ")
RadiusLabel.config(anchor = tk.W)
RadiusLabel.pack(fill = tk.BOTH)

RadiusInput = tk.Entry(root)
RadiusInput.config()
RadiusInput.pack(fill = tk.BOTH) 

HeightLabel = tk.Label(root, text = "Height: ")
HeightLabel.config(anchor = tk.W)
HeightLabel.pack(fill = tk.BOTH)

HeightInput = tk.Entry(root)
HeightInput.config()
HeightInput.pack(fill = tk.BOTH)

output = tk.Text(root)
output.config(width = 50, height = 10, state = "disabled", borderwidth = 2, relief = "groove")
output.pack(fill = tk.BOTH)

btnrun = tk.Button(root, text = "Calculate", highlightbackground = "#3E4149")
btnrun.config(fg = "blue", command = runMe)
btnrun.pack(fill = tk.BOTH)

check = tk.Checkbutton(root, text = "High Contrast")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)


root.mainloop()
print("END PROGRAM")