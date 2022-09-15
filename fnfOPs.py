import os
import fnfFolderUI as fUI
import fnfBackupLogic as fbl
import fnfFileSelectLogic as fsl
import fnfPrompts as ffp

# File Extension Change
def fileExtensionChange():
    """
    Manipulate the file extensions.
    """
    # File Extension Change mode greeting.
    print("\#\# File Format Changer \#\#")

    # First command.
    ffp.promptSelectAFolder()
    fnfFolderPath = fUI.fnfSelectFolder()
    fnfFolderPath = f"{fnfFolderPath}/"

    # Stores a list of files and directories in the fnfFolderPath.
    allFilesAndDirectoriesInDirectory = os.listdir(fnfFolderPath)

    print(f"Current files in the specified folder: {allFilesAndDirectoriesInDirectory}")
    fsl.analyzeFiles(fnfFolderPath)

    print("Which file type will be changed?")
    fromFileFormat = input()
    # Add "." if it doesnt exist.
    if fromFileFormat[0] != ".":
        fromFileFormat = f".{fromFileFormat}"

    print("To which file format it will be converted?")
    toFileFormat = input()
    # Add "." if it doesnt exist.
    if toFileFormat[0] != ".":
        toFileFormat = f".{toFileFormat}"

    print("Do you want to backup the original files? \"Yes or \"No")
    preserveOriginal = input()
    if preserveOriginal == "Yes" or "Y" or "y":
        # Selecting the original files.
        selectedFiles = fsl.selectFiles(fromFileFormat, allFilesAndDirectoriesInDirectory)
        fbl.createBackupFolder(fnfFolderPath, selectedFiles)
        # Copying the original files for backup.
        fbl.copyOriginalFiles(selectedFiles, fnfFolderPath)

    for currentFile in allFilesAndDirectoriesInDirectory:
        if fromFileFormat == os.path.splitext(currentFile)[1]:
            os.rename(currentFile, os.path.splitext(currentFile)[0] + toFileFormat)
            print(f"File changed: {currentFile}")
    
    ffp.promptApplicationExit()

def fileNameManipulator():
    """
    Manipulate file names.
    """

    # File Extension Change mode greeting.
    print("\#\# File Name Manipulator \#\#")

    ################### NAME DELETE MODE ###################
    print("\"deleteName\" -> deletes the specified word from all the files that has that word in it.")
    operationMode = input()
    print(f"You have selected {operationMode}")

    print("Which word or character do you want to remove from the files?")
    toBeDeleted = input()

    # Folder selection.
    ffp.promptSelectAFolder()
    fnfFolderPath = fUI.fnfSelectFolder()

    # Stores a list of files and directories in the fnfFolderPath.
    allFilesAndDirectoriesInDirectory = os.listdir(fnfFolderPath)
    print(f"Current files in the specified folder: {allFilesAndDirectoriesInDirectory}")

    # DELETE LOGIC
    for fnfCurrentFile in allFilesAndDirectoriesInDirectory:
        if fnfCurrentFile.find(toBeDeleted) != -1:
            fnfCurrentFilePath = f"{fnfFolderPath}{fnfCurrentFile}"
            fnfCurrentManipulatedFile = fnfCurrentFile.replace(toBeDeleted, "", 1)
            fnfManipulatedFilePath = f"{fnfFolderPath}{fnfCurrentManipulatedFile}"
            os.rename(fnfCurrentFilePath, fnfManipulatedFilePath)
    
    ffp.promptApplicationExit()