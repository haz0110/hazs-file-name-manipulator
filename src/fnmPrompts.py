def promptSelectAFolder():
    print("Please select a folder for conducting the operations.")

def promptApplicationExit():
    print("Operation completed. Type \"exit\" or press \"Control+C\" to exit.")

def help():
    # General Help that Always Prints out.
    print("""
        This is the help page.
        You can activate this page by typing "help".
        Commands you can use with this application:
            - "ffs" -> Initiates File Extension Changer. It changes the extension of all the files with the given extension.
            - "fnc" -> Initiates File Name Changer. It changes or removes the characters specified in the application.
        """)