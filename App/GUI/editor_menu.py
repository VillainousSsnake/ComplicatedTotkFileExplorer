# /App/GUI/settings_menu.py
# Contains editor menu code

# Importing modules and libraries:
import customtkinter as ctk


# editor_menu function
def editor_menu(app):

    # Detecting if the open files list is empty
    if not app.open_files:  # If the list is empty

        print("list is empty")  # TODO: Add functionality

    else:   # If the list is full

        print("the list isn't empty")   # TODO: Add functionality


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

    # TODO: Code goes here

    # Root mainloop
    root.mainloop()
