import customtkinter as ctk
from Getstarted import GetStarted
import warnings
class Main:
    def __init__(self):
            self.app = ctk.CTk()
            warnings.filterwarnings("ignore")
            self.app._set_appearance_mode("light")
            self.app.geometry("400x600")
            self.app.title('Periodoc')
            self.app.iconbitmap("menu_icon_app.ico")
            self.app.resizable(False, False)
            GetStarted(self.app)
            self.app.mainloop()
m=Main()


