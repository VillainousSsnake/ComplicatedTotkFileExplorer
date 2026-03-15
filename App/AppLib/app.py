# Higharchey/app.py
# Contains App class

# Importing Modules
from App.AppLib.config import Config


# App class
class App:
    def __init__(self):
        self.returnStatement = "main"
        self.settings = {
            "current_theme": Config.get_setting("current_theme"),
        }
        self.open_files = []
        self.supported_files = [("Text File", ('*.txt')), ("All files", "*.*")]
