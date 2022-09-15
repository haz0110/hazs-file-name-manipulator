### Imports for Folder Selection UI.
import tkinter as tk
from tkinter import filedialog
import os

# Hide the application window.
tk.Tk().withdraw()

# Select a Folder to specify the working path.
def selectFolder():
    folderPath = filedialog.askdirectory(initialdir = os.getcwd())
    folderPath = f"{folderPath}/"
    return folderPath

def listFiles(folderPath: str):
    fileList = os.listdir(folderPath)
    for currentFile in fileList:
        if os.path.isfile(f"{folderPath}{currentFile}") == 


#def listFilesAndFolders():

# Select a File to specify the path.
def selectFile():
    filePath = filedialog.askopenfilename(initialdir = os.getcwd())
    return filePath
