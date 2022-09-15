import os
import re

class fileData():
    fileType: str
    fileNameOnly: str
    name: str
    placeOfDots: list = []
    placeOfHyphens: list = []
    placeOfUnderScores: list = []
    numberOfDots: int = 0
    numberOfHyphens : int = 0
    numberOfUnderScores: int = 0
    hyphenNumberFormat: bool = False

    def __init__(self, name):
        self.name = name
        self.fileNameOnly = self.name.rsplit(".", 1)[0]
        self.fileType = self.name.rsplit(".", 1)[1]

        countDots = 0
        countHyphens = 0
        countUnderScores = 0
        currentLetterOrder = 0
        for currentLetter in self.name:
            currentName = self.name
            if currentLetter == ".":
                countDots = countDots + 1
                self.placeOfDots.append(currentLetterOrder)
            elif currentLetter == "-":
                countHyphens == countHyphens + 1
                self.placeOfHyphens.append(currentLetterOrder)
                if currentName[currentLetterOrder + 1 : len(currentName) - 2 - len(currentName.rsplit(".", 1)[1])].isdigit() == True:
                    self.hyphenNumberFormat = True
            elif currentLetter == "_":
                countUnderScores == countUnderScores + 1
                self.placeOfUnderScores.append(currentLetterOrder)
            
            currentLetterOrder = currentLetterOrder + 1
            
        self.numberOfDots = countDots
        self.numberOfHyphens = countHyphens
        self.numberOfUnderScores = countUnderScores
        
    
class folderData():

    dominantFileType: str
    folderFileList: list = []
    endWithHyphenNumber: bool = False
    fileListObject: object = []
    fileTypesList : list = []

    def __init__(self, folderPath: str):

        # using folder path, stores the file list in folderFileList
        self.folderFileList = os.listdir(folderPath)

        # creates a list of file objects in fileListObject using the fileData class.
        # this is required for further logic.
        for currentFile in self.folderFileList:
            currentFile = fileData(currentFile)
            self.fileListObject.append(currentFile)
        
        # fills the folderData.fileTypesList.
        for currentFileObject in self.fileListObject:
            self.fileTypesList.append(currentFileObject.fileType)
        
        dominantExtCounter = 0
        placeOfDominantItem = 0
        placeOfItem = 0
        for item in self.fileTypesList:
            if self.fileTypesList.count(item) > dominantExtCounter:
                dominantExtCounter = self.fileTypesList.count(item)
                placeOfDominantItem = placeOfItem
            placeOfItem = placeOfItem + 1
        
        self.dominantFileType = self.fileTypesList[placeOfDominantItem]
