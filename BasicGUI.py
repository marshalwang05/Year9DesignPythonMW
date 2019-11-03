import tkinter as tk

print("Start Program")
root = tk.Tk() 


btn1 = tk.Button(root)
btn1.config(text = "I am a button", width = 100, height = 3)
btn1.pack()

output = tk.Text(root, width = 100, height = 20)
output.config()
output.pack()

check = tk.Checkbutton(root, text = "<-- This is a click box")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)


OptionList = [
"This",
"is",
"a",
"dropdown"
] 
variable = tk.StringVar(root)
variable.set(OptionList[0])

dropdown = tk.OptionMenu(root, variable, *OptionList)
dropdown.config(width=90)
dropdown.pack()

root.mainloop()

print("END PROGRAM")