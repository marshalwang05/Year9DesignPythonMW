import tkinter as tk

root = tk.Tk()
root.title("Heat Sheet Maker")
root.geometry("1080x800") 


titlelabel = tk.Label(root, text = "Heat Sheet Maker")
titlelabel.config(width = 25, height = 2, bg = "#c5eeff", font = ("arvo bold", 25), fg = "#007691")
titlelabel.grid(column = 1, columnspan = 150, pady = 15, row = 0)

eq1 = tk.Label(root, text = "Pick Event")
eq1.config(font = ("arvo", 18), bg = "#e5f6ff")
eq1.grid(row = 1, column = 3, sticky = "e")

Events = [
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
listOfEvents = tk.OptionMenu(root, *Events)
listOfEvents.config(width=20)
listOfEvents.grid(row = 1, column = 6, sticky = "w")

SwimmerLabel = tk.Label(root, text = "Number of Swimmers:")
SwimmerLabel.config(font = ("arvo", 18), bg = "#e5f6ff")
SwimmerLabel.grid(column = 3, row = 2, sticky = "e", pady = 10)

SwimmerEntry = tk.Entry(root)	#Entry box will be used for pronoun
SwimmerEntry.config(width = 30)
SwimmerEntry.grid(column = 4, row = 2, sticky = "w", columnspan = 2)


check = tk.Button(root, text = "Create Heat Sheet")
check.config(fg = "#003274", highlightbackground = "#89dbff", width = 16, height = 2, font = ("arvo", 16))
check.grid(column = 3, columnspan = 2, row = 5, pady = 10)

highc = tk.Checkbutton(root, text = "High Contrast")	#Checkbox for high contrast
highc.config(bg = "#e5f6ff")
highc.grid(column = 1, columnspan = 1)




root.mainloop()