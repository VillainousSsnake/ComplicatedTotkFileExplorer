# /App/GUI/main_menu.py
# Contains main menu code


# Importing modules and libraries:
import customtkinter as ctk
from CTkMenuBar import *


# Class for button commands
class ButtonCommand:

    @staticmethod
    def open_settings(root, app):
        root.destroy()
        app.returnStatement = "settings"


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
    fileDropdown.add_option(option="Open", command=lambda: print("Open"))
    fileDropdown.add_option(option="Save", command=lambda: print("Save"))

    dropdown3 = CustomDropdownMenu(widget=settingsCascade)
    dropdown3.add_option(option="Configure", command=lambda: ButtonCommand.open_settings(root, app))
    dropdown3.add_option(option="Update", command=lambda: print("Update"))

    # TODO: Code goes here

    # Root mainloop
    root.mainloop()
