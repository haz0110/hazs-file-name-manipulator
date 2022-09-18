from fileinput import filename
import fnmPrompts
import tkinter as tk
from tkinter import filedialog
import os

# Hide application window.
tk.Tk().withdraw()


URLDocumentation = "https://hazarcilek.com"
userInput = "Blank"

def selectFolder():
    folderPath = filedialog.askdirectory(initialdir = os.getcwd())
    return f"{folderPath}/"

class fileData():
    filePathList: str


def fileNameChanger():
        print("Please select the working directory.")
        selectFolder()
        print("Which string you want to change?")
        nameChangedFrom = input()
        print("Which string you want to replace with?")
        nameChangedTo = input()



# Input Handler
def inputHandler(userInput: str):
    # checks to enter the file extension change function. 
    if userInput == "help":
        fnmPrompts.help()
    elif userInput == "file name change":
        fileNameChanger()


# Greeting Message and First Input
print(f"Welcome to Haz's File Name Manipulator. Type \"help\" to see usage information or visit {URLDocumentation}. Press \"Control + C\" or type \"exit\" to exit.")

# Application Loop
while userInput != "exit":
    userInput = input()
    inputHandler(userInput)


#Exit message.
print("Application terminated.")
