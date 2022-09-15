import os
import fnfData

def selectFiles(fileExtension: str, allFiles: list):
    fnfSelectedFiles = []
    for currentFile in allFiles:
        if fileExtension == str(os.path.splitext(currentFile)[1]):
            fnfSelectedFiles.append(currentFile)
    print("Selected files are: " + str(fnfSelectedFiles))

    return fnfSelectedFiles

def analyzeFiles(folderPath: str):
    fileList = os.listdir(folderPath)
    print("Analyzing the folder for probable patterns.")
    print("############")
    print(f"Most occurred file type is {fnfData.folderData(folderPath).dominantFileType}")