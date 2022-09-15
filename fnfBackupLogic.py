import os
import shutil

# Backup Folder Creator
def createBackupFolder(currentFolderPath: str, selectedFiles: list):
    """
    Takes a input of current working directory path, creates a
    folder named "fnfBackup" for storing the originals of
    manipulated files.
    """
    if currentFolderPath[-1] != "/":
        currentFolderPath = currentFolderPath + "/"

    backupFolder = "fnfBackup"
    resultingPath = currentFolderPath + backupFolder

    if os.path.exists(resultingPath) == False:
        os.mkdir(resultingPath)

def copyOriginalFiles(selectedFiles: list, currentFolderPath: str):
    for currentFile in selectedFiles:
        print(currentFolderPath)
        shutil.copyfile(f"{currentFolderPath}{currentFile}", f"{currentFolderPath}fnfBackup/{currentFile}")