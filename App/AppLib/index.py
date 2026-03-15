# App/AppLib/index.py
# Contains GUI index

# Importing GUI
from App.GUI.main_menu import main_menu as main_menu_redirect
from App.GUI.settings_menu import settings_menu as settings_menu_redirect


# Index class (Holds menu functions)
class Index:

    @staticmethod
    def main_menu(app):

        main_menu_redirect(app)

    @staticmethod
    def settings_menu(app):

        settings_menu_redirect(app)
