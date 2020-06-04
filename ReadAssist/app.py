
from tkinter import * 

import speech_recognition as sr

import json

from PIL import ImageTk, Image

def detect():
    global text
    global cur
    sentence = text[cur]
    with mic as source:
        print("speak")
        audio = r.listen(source)
        print("finished")

    try:
        response = str(r.recognize_google(audio))
        sentence = str(sentence).strip().replace(',', '').lower()
        print(response + ' - ' + sentence)
        if sentence == response:
            text[cur]="✔︎"
            cur+=1
            resetText()
            if cur == len(text)-1:
                goHome()
            else:
                return True
        else:
            print("Mismatched Messages")
            return False
    except sr.UnknownValueError:
        print("Could not understand audio")
        return False
    except sr.RequestError as e:
        print("Error; {0}".format(e))
        return False

def goHome():
    global main
    global text
    main.grid_forget()
    main = LabelFrame(root, padx=50, pady=5)
    main.grid(row = 0, column = 2)
    with open('texts.json') as file:
        data = json.load(file)
        for i in range(len(data)):
            choose_btn = Button(main, text=str(data[i]["title"]), fg="#d3d3d3", 
                font=("Geneva", 20, "normal"), borderwidth=0,
                activeforeground="orange", command=lambda j=i: goReadText(data[j]["content"]))
            choose_btn.grid()

def resetText():
    global main
    global text
    main.grid_forget()
    main = LabelFrame(root, padx=50, pady=5)
    main.grid(row = 0, column = 2)
    for i in range(len(text)-1):
        sentence = text[i].strip()
        if i == cur:
            Label(main, text=sentence, fg="orange").grid(row=i, column=0)
        else:
            Label(main, text=sentence).grid(row=i, column=0)

def goReadText(content):
    print(content)
    global main
    global text
    global cur
    cur = 0
    main.grid_forget()
    main = LabelFrame(root, padx=50, pady=5)
    main.grid(row = 0, column = 2)
    text = content
    text = text.split(".")
    for i in range(len(text)-1):
        sentence = text[i].strip()
        if i == cur:
            Label(main, text=sentence, fg="orange").grid(row=i, column=0)
        else:
            Label(main, text=sentence).grid(row=i, column=0)

def goAdd():
    global main
    main.grid_forget()
    main = LabelFrame(root, padx=50, pady=100)
    main.grid(row = 0, column = 2)
    title_name = Label(main, text="Title").grid(row=0, column=0)
    title = Entry(main)
    title.grid(row=0, column=1)
    content_name = Label(main, text="Content").grid(row=1, column=0)
    content = Entry(main)
    content.grid(row=1, column=1)
    finish_btn = Button(main, text="Add", fg="#d3d3d3", 
        font=("Geneva", 20, "normal"), borderwidth=0,
        activeforeground="orange", command=lambda: finishAdd(title.get(), content.get()))
    finish_btn.grid(row = 3, column = 1)

def finishAdd(title, content):
    write = {"title":title, "content":content}
    temp = "";
    with open('texts.json') as file:
        data = json.load(file)
        temp = data
        temp.append(write)
    with open("texts.json",'w') as f: 
        json.dump(temp, f, indent=2) 
    goHome()

def goDelete():
    global main
    main.grid_forget()
    main = LabelFrame(root, padx=50, pady=5)
    main.grid(row = 0, column = 2)
    note = Label(main, text="Pick text to remove").grid(row=0, column=0)
    with open('texts.json') as file:
        data = json.load(file)
        for i in range(len(data)):
            choose_btn = Button(main, text=str(data[i]["title"]), fg="#d3d3d3", 
                font=("Geneva", 20, "normal"), borderwidth=0,
                activeforeground="orange", command=lambda j=i: finishDelete(data[j]["title"], data[j]["content"]))
            choose_btn.grid()

def finishDelete(title, content):
    write = {"title":title, "content":content}
    temp = "";
    with open('texts.json') as file:
        data = json.load(file)
        temp = data
        temp.remove(write)
    with open("texts.json",'w') as f: 
        json.dump(temp, f, indent=2)
    goHome()

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("Adjusting audio - be quiet")
    r.adjust_for_ambient_noise(source)
    print("Finished adjustments")

text = ""

cur = 0

root = Tk()
root.title("Reading Assistance Program")
root.geometry('700x700')

root.configure(bg='navy')

sidebar = LabelFrame(root, text="ReadAssist")
sidebar.grid(row = 0, column = 0, rowspan = 4)

logo = ImageTk.PhotoImage(Image.open("Logo-100x100.png"))
logo_label = Label(sidebar, image=logo)
logo_label.grid(row=0, column=0, padx=10, pady=10)

speak_btn = Button(sidebar, text="Speak", fg="#d3d3d3", 
    font=("Geneva", 20, "normal"), borderwidth=0,
    activeforeground="orange", command=detect)
speak_btn.grid(row = 1, column = 0)

home_btn = Button(sidebar, text="Home", fg="#d3d3d3", 
    font=("Geneva", 20, "normal"), borderwidth=0,
    activeforeground="orange", command=goHome)
home_btn.grid(row = 2, column = 0)

add_btn = Button(sidebar, text="Add", fg="#d3d3d3", 
    font=("Geneva", 20, "normal"), borderwidth=0,
    activeforeground="orange", command=goAdd)
add_btn.grid(row = 3, column = 0)

delete_btn = Button(sidebar, text="Delete", fg="#d3d3d3", 
    font=("Geneva", 20, "normal"), borderwidth=0,
    activeforeground="orange", command=goDelete)
delete_btn.grid(row = 4, column = 0)

main = LabelFrame(root, padx=100, pady=200)
main.grid(row = 1, column = 2)

title_name = Label(main, text="Title").grid(row=0, column=0)
title = Entry(main).grid(row=0, column=1)
content_name = Label(main, text="Content").grid(row=1, column=0)
content = Entry(main).grid(row=1, column=1)

title_name = Label(main, text="Title").grid(row=0, column=0)
title = Entry(main).grid(row=0, column=1)
content_name = Label(main, text="Content").grid(row=1, column=0)
content = Entry(main).grid(row=1, column=1)

goHome()

root.mainloop()

















