import customtkinter as ctk
from PIL import Image,ImageTk
from First_Page import FirstPage
from Log_In import Login

class GetStarted():
    def __init__(self,app):
        #Window app
        self.app=app
        # Creating frame of window size
        self.frame=ctk.CTkFrame(
            self.app,
            fg_color="#DC6E87"
        )
        self.frame.pack(fill="both",expand=True)
        #Name Label app
        label=ctk.CTkLabel(
            self.frame,
            text="Periodoc",
            font=("Bahnschrift Light Condensed",50),
            text_color="white"
        )
        label.pack(padx=15,pady=20)
        #Adding image of calender at middle of frame
        self.path="cal.png"
        self.bg_img = Image.open(self.path)
        self.bg_ctk_img = ctk.CTkImage(self.bg_img, size=(300, 200))
        self.bg_img_label = ctk.CTkLabel(
            self.frame,
            text="",
            image=self.bg_ctk_img
        )
        self.bg_img_label.pack(padx=20,pady=20)
        #Tagline of app
        text_label=ctk.CTkLabel(
            self.frame,
            text_color="white",
            text="Track your period cycle and\n "
            "stay tension free everyday.\n "
            "It's time to love yourself!",
            font=("Bahnschrift Light Condensed",25)
        )
        text_label.pack(pady=30)
        #Get started button move to next page
        GetStarted_But=ctk.CTkButton(
            self.frame,
            text_color="black",
            text="Get Started",
            font=("Bahnschrift Light Condensed",20),
            corner_radius=5,
            fg_color="white",
            hover_color="#F9C1CB",
            height=50,
            width=200,
            command=lambda:self.open_next_page_command()
        )
        GetStarted_But.pack(padx=10,pady=35)

    def open_next_page_command(self):
        self.frame.destroy()
        FirstPage(self.app)  # Open next page in the same window


