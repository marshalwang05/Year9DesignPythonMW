import tkinter as tk
from tkinter import messagebox
import csv

#variables

events = [
"50 Free",
"100 Free",
"200 Free",
"50 Fly",
"100 Fly",
"200 Fly",
"50 Breast",
"100 Breast",
"200 Breast",
"50 Back",
"100 Back",
"200 Back",
"100 IM",
"200 IM",
"400 IM",
]
#Widget lists
inputName = []
inputTime = []
inputTeam = []
 
#Data lists
dataName = []
dataTime = []
dataTeam = []


#function

def on_closing():
	if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
		root.destroy()

def enable():
	listOfEvents.config(state='normal')
	swimmerEntry.config(state='normal')

	#Copy all information into data structure (lists)

	for i in range *(0, len(inputName), 1):
		dataName.append(inputName[i].get())
		dataTime.append(inputName[i].get())
		dataTeam.append(inputName[i].get())


	#Destroy all of the fields


	print(inputName)
	#Counted loop
	for i in range (0, len(inputName), 1):
		inputName[i].destroy()
		inputTime[i].destroy()
		inputTeam[i].destroy()

	#Conditional loop
	while (len(inputName)>0):
		inputName.pop(0)
		inputTime.pop(0)
		inputTeam.pop(0)

	print(inputName)



def enterPress(*args):
  
  listOfEvents.config(state='disabled')
  swimmerEntry.config(state='disabled')

  val = int (swimmerEntry.get())

  for i in range (0, val, 1):

    inputName.append(tk.Entry(root))  
    inputName[i].config(width = 15)
    inputName[i].grid(column = 2, row = 7+2*i, sticky = "w", columnspan = 2)

    inputTeam.append(tk.Entry(root))  
    inputTeam[i].config(width = 15)
    inputTeam[i].grid(column = 6, row = 7+2*i, sticky = "w", columnspan = 2) 

    inputTime.append(tk.Entry(root))  
    inputTime[i].config(width = 15)
    inputTime[i].grid(column = 3, row = 7+2*i, columnspan = 2) 


def hcontrast():

  state = highco.get()
  #High Contrast
  if state == 1:
    
    root.config(bg="black")
    titlelabel.config(bg = "#000058", fg = "white")
    pickEventLabel.config(bg = "#000058", fg = "white")
    swimmerLabel.config(bg = "#000058", fg = "white")
    hLine.config(bg = "black", fg = "white")
    inputNameLabel.config(bg = "#000058", fg = "white")
    inputTimeLabel.config(bg = "#000058", fg = "white")
    inputTeamLabel.config(bg = "#000058", fg = "white")
    create.config(bg = "#000058", fg = "white")

  # Normal Contrast

  if state == 0:
    root.config(bg="white")
    titlelabel.config(bg = "#c5eeff", fg = "#007691")
    pickEventLabel.config(bg = "#e5f6ff", fg = "black")
    listOfEvents.config(bg = "white", fg = "black")
    swimmerLabel.config(bg = "#e5f6ff", fg = "black")
    hLine.config(bg = "white", fg = "black")
    inputNameLabel.config(bg = "white", fg = "black")
    inputTimeLabel.config(bg = "white", fg = "black")
    inputTeamLabel.config(bg = "white", fg = "black")
    create.config(bg = "#", fg = "#black")

    

#main code


root = tk.Tk()
root.title("Heat Sheet Maker")


titlelabel = tk.Label(root, text = "Heat Sheet Maker")
titlelabel.config(width = 25, height = 2, bg = "#c5eeff", font = ("arvo bold", 25), fg = "#007691")
titlelabel.grid(column = 3, columnspan = 3, pady = 15, row = 0)

pickEventLabel = tk.Label(root, text = "Pick Event")
pickEventLabel.config(font = ("arvo", 18), bg = "#e5f6ff", width = 20)
pickEventLabel.grid(row = 1, column = 3, sticky = "e")

var = tk.StringVar(root)
var.set(events[0])
listOfEvents = tk.OptionMenu(root, var, *events)
listOfEvents.config(width=20)
listOfEvents.grid(row = 1, column = 4, sticky = "w",)

swimmerLabel = tk.Label(root, text = "Number of Swimmers:")
swimmerLabel.config(font = ("arvo", 18), bg = "#e5f6ff", width = 20)
swimmerLabel.grid(column = 3, row = 2, sticky = "w", pady = 10)

swimmerEntry = tk.Entry(root) 
swimmerEntry.config(width = 20)
swimmerEntry.bind('<Return>', enterPress)
swimmerEntry.grid(column = 4, row = 2, sticky = "w", columnspan = 2)


hLine = tk.Label(root, text = "----------------------------------------------------------------------------------------------------------------")
hLine.config()
hLine.grid(column = 0, row = 3, sticky = "w", columnspan = 10)

inputNameLabel = tk.Label(root, text = "Input Name")
inputNameLabel.config(font = ("arvo", 18), bg = "#e5f6ff")
inputNameLabel.grid(column = 2, row = 6, sticky = "w", pady = 10)


inputTimeLabel = tk.Label(root, text = "Input Time:")
inputTimeLabel.config(font = ("arvo", 18), bg = "#e5f6ff")
inputTimeLabel.grid(column = 3, row = 6, pady = 10, columnspan = 2)


inputTeamLabel = tk.Label(root, text = "Input Team:")
inputTeamLabel.config(font = ("arvo", 18), bg = "#e5f6ff")
inputTeamLabel.grid(column = 6, row = 6, sticky = "w", pady = 10)



create = tk.Button(root, text = "Create Heat Sheet:")
create.config(width = 25, height = 2, bg = "#c5eeff", font = ("arvo bold", 16), fg = "#007691", command = enable)
create.grid(column = 1, columnspan = 150, pady = 15, row = 800)

highco = tk.IntVar()
highc = tk.Checkbutton(root, text = "High Contrast")  #Checkbox for high contrast
highc.config(bg = "#e5f6ff", command = hcontrast, variable = highco, onvalue = 1, offvalue = 0)
highc.grid(column = 2, columnspan = 1,)

root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()