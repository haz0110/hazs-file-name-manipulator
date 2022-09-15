import fnfOPs
import fnfHelp

URLDocumentation = "https://hazarcilek.com"
level1UserInput = "Blank"

# Input Handler
def inputHandler(level1UserInput: str):
    # checks to enter the file extension change function. 
    if level1UserInput == "help":
        fnfHelp.help()
    # checks to enter the file name manipulator function.
    # this function is rather big and consists of many other functions.
    elif level1UserInput == "fnm":
        fnfOPs.fileNameManipulator()

# Greeting Message and First Input
print(f"Welcome to Haz's File Name Manipulator. Type \"help\" to see usage information or visit {URLDocumentation}. Press \"Control + C\" or type \"exit\" to exit.")

# Application Loop
while level1UserInput != "exit":
    level1UserInput = input()
    inputHandler(level1UserInput)


#Exit message.
print("Application terminated.")
