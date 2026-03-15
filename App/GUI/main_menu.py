# /App/GUI/main_menu.py
# Contains main menu code


# Importing modules and libraries:
import customtkinter as ctk
from CTkMenuBar import *
from tkinter import filedialog


# Class for button commands
class ButtonCommand:

    @staticmethod
    def open_settings(root, app):

        # Destroying the root and launchign settings
        root.destroy()
        app.returnStatement = "settings"

    @staticmethod
    def open_editor(root, app, explorerType):
        """
        Opens the editor menu
        :param root: CTk Root Window
        :param app: App Object
        :param explorerType: String obj. OPTIONS: 'file' - selects one file, 'folder' - opens folder
        """

        # Detecting which filedialog needs to be launched
        match explorerType:

            case 'file':    # Opening a single file

                # Adding a file to the open files list
                app.open_files.append(
                    filedialog.askopenfilename(
                        title="Open a file...",
                        filetypes=app.supported_files
                    )
                )

            case 'folder':  # Opening a whole folder
                pass    # TODO: Stub

            case _:
                print("Throw Error")    # TODO: Add throw error functionality

        # Destroying root and launching editor
        root.destroy()
        app.returnStatement = "editor"


# main_menu function
def main_menu(app):

    # Creating root window
    root = ctk.CTk()
    root.title("Main  ")
    root.geometry("850x525+200+200")

    # Defining on_close function
    def on_close():
        root.destroy()
        app.returnStatement = "exit"

    # Assigning the buttons on the tkinter window top bar
    root.protocol("WM_DELETE_WINDOW", on_close)

    menu = CTkTitleMenu(root)
    fileCascade = menu.add_cascade("File")
    settingsCascade = menu.add_cascade("Settings")

    fileDropdown = CustomDropdownMenu(widget=fileCascade)
    fileDropdown.add_option(option="Open File", command=lambda: ButtonCommand.open_editor(root, app, "file"))
    fileDropdown.add_option(option="Open Folder", command=lambda: print("Open Folder"))  # TODO: Implement cmd

    settingsDropdown = CustomDropdownMenu(widget=settingsCascade)
    settingsDropdown.add_option(option="Configure", command=lambda: ButtonCommand.open_settings(root, app))
    settingsDropdown.add_option(option="Update", command=lambda: print("Update"))   # TODO: Implement cmd

    # TODO: Code goes here

    # Root mainloop
    root.mainloop()
