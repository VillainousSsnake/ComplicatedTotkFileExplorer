# /App/GUI/settings_menu.py
# Contains settings menu code

# Importing modules and libraries:
import customtkinter as ctk
from App.AppLib.config import Config


# settings_menu function
def settings_menu(app):

    # Creating root window
    root = ctk.CTk()
    root.title("Configure Settings...  ")
    root.geometry("850x525+200+200")

    # Defining on_close function
    def on_close():
        root.destroy()
        app.returnStatement = "exit"

    # Assigning the buttons on the tkinter window top bar
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Getting settings dictionary
    all_settings = Config.get_all_settings()
    print(all_settings)    # TODO: Remove print statement

    # TODO: Code goes here

    # Root mainloop
    root.mainloop()
