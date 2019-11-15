import tkinter as tk

print("Start Program")
root = tk.Tk()
root.title

#Title
title = tk.Label(root, text = "Heat Sheet Maker")
title.config(width = 25, height = 2, bg="#c5eeff", font = ("arvo bold", 25), fg = "#007691")
title.grid(columnspan = 5, pady=15, row=0)


OptionList = [
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
variable = tk.StringVar(root)
variable.set(OptionList[0])

dropdownlabel = tk.Label(root, text = "Pick Event")
dropdownlabel.config(anchor = tk.W)
dropdownlabel.pack(fill = tk.BOTH)

dropdown = tk.OptionMenu(root, variable, *OptionList)
dropdown.config(width=45)
dropdown.pack()


SwimmerNumber = tk.Label(root, text = "Number of Swimmers: ")
SwimmerNumber.config(anchor = tk.W)
SwimmerNumber.pack(fill = tk.BOTH)

SwimmerNumberBox = tk.Entry(root)
SwimmerNumberBox.config()
SwimmerNumberBox.pack(fill = tk.BOTH)


root.mainloop()
print("End Program")