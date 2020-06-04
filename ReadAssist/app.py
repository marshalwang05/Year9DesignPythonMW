# 1) Put folder where you want it on your computer
# 2) Open terminal
# 3) Type 'cd ' and the path to the folder
# For example, if this folder, 'ReadAssist' is in the a folder called 'Python' in the 'Documents' folder, you would type 'cd Documents/Python'
# Or if this folder were on your Desktop, you would type 'cd Desktop'
# 4) Type the following one after another in terminal (the first one may take a couple minutes)

# /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# brew install portaudio
# pip install -r requirements.txt

# The first one installs HomeBrew, which is needed for PyAudio
# The second installs PortAudio, which is also needed for PyAudio
# The third one is equivalent to the followng three commands:

# pip install PyAudio
# pip install pillow
# pip install SpeechRecognition

# Which installs PyAydio, pillow, and SpeechRecognition respectively

# 5) You run this code by typing 'python app.py' into your terminal (make sure you've type the cd command in step 3)
# This assumes you've downloaded python already
# What it does is runs this file using python
# I used Python 3.7.6 but any above 3 should probably work

# 6) You can replace the file called 'Logo-100x100' with another 100x100 image, just make sure it has the same name of 'Logo-100x100'
# You might have to move or delete the original 'Logo-100x100'

# imports tkinter
from tkinter import * 

# imports SpeechRecognition as variable sr, a package used to recognize words from audio
import speech_recognition as sr

# imports json, which is a built-in python package used to handle, you guessed it, JSON's
import json

# imports ImageTk and Image classes from pillow, a package used to handle images
from PIL import ImageTk, Image

# Note, I suggest you skip down until the ––––––––– at the bottom, and then go back up to read this part below

# This function is the one that listens for talking in the microphone, then translates that audio into words, then compares it with the line of text
def detect():
    # Get the variable text, defined below
    # global is needed since we didn't pass it into the function yet still need it
    # What global does is essentially get a variable from "anywhere" on the file that's not in a function
    # Text is the paragraph or array of the sentences which the user should read
    global text
    # Gets the varable cur so we know which line we're on
    global cur
    # Gets the current line and stores it in a variable called sentence, which will be used to compare to the user's speech
    sentence = text[cur]
    # As mentioned before, this opens the mic
    with mic as source:
        print("speak")
        # This listens for sound, and will end when no more audio is detected for a short period of time
        # Stores it in a variable called audio
        audio = r.listen(source)
        print("finished")

    # Try catch/except block, which tries to do something
    # If that thing works, great
    # If it doesn't the except blocks below will try and catch any errors that the code throws
    # And do something based off of that error
    try:
        # Uses the Google Speech API (I think), which is built into SpeechRecognition, to find words in the audio variable
        response = str(r.recognize_google(audio))
        # Replaces all the comma's in the sentence which is being compared and turns all the characters to lowercase
        # This is needed becuase the string that google returns (see above), is an all lowercase string without commas
        sentence = str(sentence).strip().replace(',', '').lower()
        print(response + ' - ' + sentence)
        # If the response is equal to the sentence
        if sentence == response:
            # Replace the current index of the text array, which was the sentence being compared, see line 54, with a checkmark
            text[cur]="✔︎"
            # Add 1 to the current counter, which moves onto the next line
            cur+=1
            # Calls the 'resetText' function, which reloads the 'main' frame so that the checkmark(s) appear
            resetText()
            # If the sentence that was just gotten correct is the last sentence in the text, send the user back to the home page
            if cur == len(text)-1:
                # This functino 'goHome' sends the user to the home page
                goHome()
            else:
                # Otherwise, return the function
                # The 'True' part isn't needed, but it's keep it there for organization's sake (Read: too lazy to get rid of)
                return True
        # If what the user said and what the sentence is DOESN'T match, print out 'Mismatched Messages'
        else:
            print("Mismatched Messages")
            # Ends function
            # Again 'False' isn't needed but it's there for organization
            return False
    except sr.UnknownValueError:
        # If the microphone doesn't detect any words or any audio
        print("Could not understand audio")
        return False
    except sr.RequestError as e:
        # A request error, which is likely due to lack of internet connection, as 'recognize_google' (line 69), needs an internet connection
        print("Error; {0}".format(e))
        return False

# Sends user to home page
def goHome():
    # Gets main, which was defined below
    global main
    # Gets text, which now that I look at it, was probably uneccessary
    global text
    # Deletes the 'main' frame, which also removes anything inside, which is used to reset the page
    main.grid_forget()
    # Creates a new 'main' frame
    main = LabelFrame(root, padx=50, pady=5)
    # Adds it to the window
    main.grid(row = 0, column = 2)
    # Opens the texts.json file, which is used to store all the texts and titles of the texts
    with open('texts.json') as file:
        # Sets variable data as the object inside the json
        data = json.load(file)
        # Loops through the data object, which is ok, as the data object is an array which stores dictionaries with the instances 'title' and 'content'
        # Open texts.json to take a look
        for i in range(len(data)):
            # Creates a button for each dictionary in the data array, that, when clicked, calls the goReadText with the content of the text passed in
            # lambda creates an anonlymous function, which calls goReadText
            # goReadText needs to be passed in the content, the reason lambda is needed, as you can't do it otherwise
            choose_btn = Button(main, text=str(data[i]["title"]), fg="#d3d3d3", 
                font=("Geneva", 20, "normal"), borderwidth=0,
                activeforeground="orange", command=lambda j=i: goReadText(data[j]["content"]))
            # Adds the button to the bottom of the 'main' frame
            choose_btn.grid()

# Used to reload the 'main' frame when reading
def resetText():
    # Gets the main variable
    global main
    # Gets the text variable, which contains the array which holds the sentences the user is reading
    global text
    # Resets the 'main' frame
    main.grid_forget()
    main = LabelFrame(root, padx=50, pady=5)
    main.grid(row = 0, column = 2)
    # Loops through each sentence in the text array
    for i in range(len(text)-1):
        # Removes any trailing spaces in the sentence
        sentence = text[i].strip()
        # If the sentence is the current sentence that the user should read, make it orange, otherwise, make it normal
        if i == cur:
            Label(main, text=sentence, fg="orange").grid(row=i, column=0)
        else:
            Label(main, text=sentence).grid(row=i, column=0)

# Takes the user to the reading page
def goReadText(content):
    print(content)
    # Gets main, text, and cur variables
    global main
    global text
    global cur
    # Resets the current counter to 0, as when opening a new text, it should automatically start at the beginning
    cur = 0
    # Resets 'main' frame
    main.grid_forget()
    main = LabelFrame(root, padx=50, pady=5)
    main.grid(row = 0, column = 2)
    # Set the text equal to the content string
    text = content
    # Turns the text into an array, split into strings every time there is a period
    # NOTE: THIS MEANS SENTENCES ENDING WITH A ! OR A ?, OR EVEN WITH A ; INSIDE WILL NOT WORK
    # Why, you ask, don't you make it work, then?
    # no
    text = text.split(".")
    # Loops through the length of the text
    # NOTE: THIS ASSUMES THE LAST SENTENCE OF THE TEXT WILL END IN A PERIOD, OTHERWISE THE LAST SENTENCE OF THE TEXT WILL BE SKIPPED
    for i in range(len(text)-1):
        # Removes any trailing spaces
        sentence = text[i].strip()
        # If it's the current sentence the user should read, make it orange
        if i == cur:
            Label(main, text=sentence, fg="orange").grid(row=i, column=0)
        else:
            Label(main, text=sentence).grid(row=i, column=0)

# Send the user to the add page, where they can add another text
def goAdd():
    # Get and reset main
    global main
    main.grid_forget()
    main = LabelFrame(root, padx=50, pady=100)
    main.grid(row = 0, column = 2)
    # Create a title text box for the title of the text
    title_name = Label(main, text="Title").grid(row=0, column=0)
    title = Entry(main)
    title.grid(row=0, column=1)
    # Create a content text box, for the content of the text
    content_name = Label(main, text="Content").grid(row=1, column=0)
    content = Entry(main)
    content.grid(row=1, column=1)
    # Creates a finish button once the user has finished typing everything
    # Calls teh finishAdd function, and passes in the values in the title and content
    # NOTE: THIS MEANS THERE CANNOT BE TWO TEXTS WITH THE SAME TITLE, THE FIRST WILL BE GOTTEN OR THERE WILL BE AN ERROR
    finish_btn = Button(main, text="Add", fg="#d3d3d3", 
        font=("Geneva", 20, "normal"), borderwidth=0,
        activeforeground="orange", command=lambda: finishAdd(title.get(), content.get()))
    finish_btn.grid(row = 3, column = 1)

# Adds the values title and content to the json file
def finishAdd(title, content):
    # Create dictionary write and put the title and content in
    write = {"title":title, "content":content}
    # Create temporary variable
    temp = "";
    # Open the json file and set the data inside to variable 'data'
    with open('texts.json') as file:
        data = json.load(file)
        # Set temp as data and add the write dictionary to the end
        temp = data
        temp.append(write)
    # Open the json file in writing form
    with open("texts.json",'w') as f: 
        # Dump the new object into the file
        json.dump(temp, f, indent=2) 
    # Send the user to the home page, which should now have the new text
    goHome()

# Deletes a text from the page
def goDelete():
    # Gets and resets the 'main' frame
    global main
    main.grid_forget()
    main = LabelFrame(root, padx=50, pady=5)
    main.grid(row = 0, column = 2)
    # Adds a text with the instructions
    note = Label(main, text="Pick text to remove").grid(row=0, column=0)
    # Adds a button for every text in the json file, that, when clicked, activates the finishDelete function, with the tile and content of the text passed in
    with open('texts.json') as file:
        data = json.load(file)
        for i in range(len(data)):
            choose_btn = Button(main, text=str(data[i]["title"]), fg="#d3d3d3", 
                font=("Geneva", 20, "normal"), borderwidth=0,
                activeforeground="orange", command=lambda j=i: finishDelete(data[j]["title"], data[j]["content"]))
            choose_btn.grid()

# Deletes the dictionary with the same title and content as the ones passed in
def finishDelete(title, content):
    # Creates the dictionary that should match the one being deleted
    write = {"title":title, "content":content}
    # Tempoarary variable
    temp = "";
    with open('texts.json') as file:
        data = json.load(file)
        temp = data
        # Removes the matching dictioary from the json file
        temp.remove(write)
    with open("texts.json",'w') as f: 
        # Updates the json file
        json.dump(temp, f, indent=2)
    # Sends the user back to the home page
    goHome()

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Below is where the actual code starts and defining functions ends

# Recognizer class from SpeechRecognition
r = sr.Recognizer()
# Microphone class from SpeechRecognition
mic = sr.Microphone()
# This opens the mic - imagine a book, you have to open the book first to read it, and then you have to close it - that's what this with thing does
with mic as source:
    print("Adjusting audio - be quiet")
    # This line adjusts the microphone to fit the ambient sound in the background beforehand
    # Not really necessary if you are in a complete silent room, but it's recommended
    r.adjust_for_ambient_noise(source)
    print("Finished adjustments")

# Creates variable 'text' which will be used to store the text the user should read out
text = ""

# Creates variable 'cur' which keeps track of which line the user is reading or supposed to read
cur = 0

# Creates the window the UI(you know, the visuals and stuff) will be on
root = Tk()
# Title of the window
root.title("Reading Assistance Program")
# Size of the window
root.geometry('700x700')

root.configure(bg='navy')

# Creates a frame called sidebar with the title 'ReadAssist'
sidebar = LabelFrame(root, text="ReadAssist")
# Adds the frame onto the window, at row 0, column 0, which will take up 4 rows
sidebar.grid(row = 0, column = 0, rowspan = 4)

# Get the image
logo = ImageTk.PhotoImage(Image.open("Logo-100x100.png"))
# Creates a label with the logo image
logo_label = Label(sidebar, image=logo)
# Adds it to the sidebar frame, with a padding on all sides of 10
logo_label.grid(row=0, column=0, padx=10, pady=10)

# Creates a speak button with the text 'Speak' and text color #d3d3d3
# It has the font Geneva, with size 20, and is normal (not bold)
# Has a border width of 0 (I don't think that actually does anything)
# Turns orange when you click on it, and when clicked, calls/activates on the function named 'detect'
speak_btn = Button(sidebar, text="Speak", fg="#d3d3d3", 
    font=("Geneva", 20, "normal"), borderwidth=0,
    activeforeground="orange", command=detect)
# Adds it to the sidebar frame at row 1 column 0, which means it's under the logo image
speak_btn.grid(row = 1, column = 0)

# Same thing as the speak_btn, except function 'goHome' is called instead of 'detect'
home_btn = Button(sidebar, text="Home", fg="#d3d3d3", 
    font=("Geneva", 20, "normal"), borderwidth=0,
    activeforeground="orange", command=goHome)
# On row 2, which is under row 1, where speak_btn is
home_btn.grid(row = 2, column = 0)

# Same as speak_btn, but calls 'goAdd'
add_btn = Button(sidebar, text="Add", fg="#d3d3d3", 
    font=("Geneva", 20, "normal"), borderwidth=0,
    activeforeground="orange", command=goAdd)
add_btn.grid(row = 3, column = 0)

# Same as speak_btn, but calls 'goDelete'
delete_btn = Button(sidebar, text="Delete", fg="#d3d3d3", 
    font=("Geneva", 20, "normal"), borderwidth=0,
    activeforeground="orange", command=goDelete)
delete_btn.grid(row = 4, column = 0)

# Creates a frame called 'main', like the 'sidebar', which has a x-padding of 100 and y-padding of 200
# Note the difference between padding in the LabelFrame and the paddin when you call grid
# Padding in LabelFrame means the padding on the inside of the frame, pushing the border outwards
# Padding when you call grid (not demonstrated here) changes the padding AROUND the frame, so it will distance the frame from other components
main = LabelFrame(root, padx=100, pady=200)
# Don't ask why I put the column as 2, I have no idea, it works too it it's 0, but I'm too lazy to change it everytime I did it (See: functions above)
main.grid(row = 1, column = 2)

# All the stuff below from point A to B will be removed, but I needed to create the variables first, so I could use them later
# Is explained in the functions
# A
title_name = Label(main, text="Title").grid(row=0, column=0)
title = Entry(main).grid(row=0, column=1)
content_name = Label(main, text="Content").grid(row=1, column=0)
content = Entry(main).grid(row=1, column=1)

title_name = Label(main, text="Title").grid(row=0, column=0)
title = Entry(main).grid(row=0, column=1)
content_name = Label(main, text="Content").grid(row=1, column=0)
content = Entry(main).grid(row=1, column=1)
# B

# Calls on the function 'goHome'
goHome()

# This is the window loop, which is necessary for any tkinter app to work
root.mainloop()

















