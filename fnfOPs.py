import os
import fnfFolderUI as fUI
import fnfPrompts as ffp
from fnfData import fileData, folderData
import re

modeDelete = "delete"

def fnmDeleteMode(folderPath: str):

    print("Which word or character do you want to remove from the files?")
    toBeDeleted = input()

    # Stores a list of files and directories in the folderPath.
    allDirectory = folderData(folderPath)
    print(f"Current files in the specified folder: {allDirectory.folderFileList}")

    # DELETE LOGIC
    # TO BE FILLED
    


def fileNameManipulator():
    """
    Manipulate file names.
    """

    # File Extension Change mode greeting.
    print("\#\# File Name Manipulator \#\#")

    # Folder selection.
    ffp.promptSelectAFolder()
    folderPath = fUI.selectFolder()

    # Available Modes
    print(f"\"{modeDelete}\" -> enters the delete mode.")
    operationMode = input()
    print(f"You have selected \"{operationMode}\" mode")
    if operationMode == modeDelete:
        fnmDeleteMode(folderPath)


    ffp.promptApplicationExit()