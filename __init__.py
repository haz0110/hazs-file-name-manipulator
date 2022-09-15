import fnfHelp
import fnfOPs

# GLOBAL CONSTANTS
URLDocumentation = "https://hazarcilek.com"

# GLOBAL VARIABLES
fnfUserInput = "Blank"

# Input Handler
def fnfInputHandler(fnfInput: str):
    if fnfInput == "ffs":
        fnfOPs.fileExtensionChange()
    elif fnfInput == "help":
        fnfHelp.help()
    elif fnfInput == "fnm":
        fnfOPs.fileNameManipulator()

# Greeting Message and First Input
print(f"Welcome to File Name Formatter. Type \"help\" to see usage information or visit {URLDocumentation}. Press \"Control + C\" or type \"exit\" to exit.")

# Application Loop
# Always check the input if it is 
while fnfUserInput != "exit":
    fnfUserInput = input()
    # Experimental ?? Checks the help message always so it can show the documentation in every part of the application.
    if fnfUserInput == "help":
        # Calls the help function from the fnfHelp.py
        fnfHelp.help()
    # Handles the inputs and directs the application between files.
    fnfInputHandler(fnfUserInput)


#Exit message.
print("Application terminated.")
