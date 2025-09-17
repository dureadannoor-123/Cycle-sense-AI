import customtkinter as ctk
from PIL import Image,ImageTk

class FirstPage:
    def __init__(self,app):
        #window app
        self.app=app
        # Full Frame
        self.frame = ctk.CTkFrame(
            self.app,
            fg_color="#DC6E87"
        )
        self.frame.pack(fill="both", expand=True)
        # upper frame image
        self.upper_frame_img = ImageTk.PhotoImage(Image.open("half-removebg-preview.png"))
        #Second Half frame
        self.frame2 = ctk.CTkFrame(
            self.app,
            fg_color="#DC6E87"
        )
        self.frame2.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        self.label = ctk.CTkLabel(self.frame2,
            image=self.upper_frame_img,
            text=""
        )
        self.label.place(relx=0, rely=0, relwidth=1, relheight=1)
        #Back Button
        back_button_pic = ImageTk.PhotoImage(Image.open("back_button.png").resize((30, 30)))
        back_button = ctk.CTkButton(
             self.frame2,
             image=back_button_pic,
             text="",
             fg_color="#DC6E87",
             hover_color="#FECCCB",
             width=0,
             height=0,
             cursor="hand2",
             command=lambda: self.back_button_command()
        )
        back_button.place(x=25, y=25)
        #Name of app label
        Label = ctk.CTkLabel(
            self.frame,
            text_color="white",
            text="Periodoc",
            font=("Bahnschrift Light ", 30, "bold")
        )
        Label.place(x=135, y=295)
        # Tagline Label
        Label = ctk.CTkLabel(
            self.frame,
            text_color="white",
            text="Your Cycle, Your Power!\nTrack, Predict, and Stay in Control.",
            font=("Bahnschrift Light ", 20)
        )
        Label.place(x=56, y=340)
        #Login Button
        Login = ctk.CTkButton(self.frame,
           text="LOGIN ",
           corner_radius=10,
           height=40,
           width=260,
           fg_color="#B43D3A",
           font=("Bahnschrift Light ", 20, "bold"),
           text_color="white",
           hover_color="#FECCCB",
           command=lambda:self.login_page_Command()
        )
        Login.place(x=70, y=430)
        #SIgn Up Button
        SignUp = ctk.CTkButton(
            self.frame,
            text="SIGN UP ",
            corner_radius=10,
            height=40,
            width=260,
            fg_color="#B43D3A",
            font=("Bahnschrift Light ", 20, "bold"),
            text_color="white",
            hover_color="#FECCCB",
            command=lambda:self.Signup_Command()
        )
        SignUp.place(x=70, y=490)
    def back_button_command(self):
        from Getstarted import GetStarted
        self.frame.destroy()
        self.frame2.destroy()

        GetStarted(self.app)
    def login_page_Command(self):
        from Log_In import Login
        self.frame.destroy()
        self.frame2.destroy()
        Login(self.app)
    def Signup_Command(self):
        from SignUp import Sign_UP
        self.frame.destroy()
        self.frame2.destroy()

        Sign_UP(self.app)
