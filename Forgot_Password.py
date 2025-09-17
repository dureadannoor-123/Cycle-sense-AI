from PIL import Image,ImageTk
import customtkinter as ctk
from tkinter import messagebox
from numpy.ma.core import resize
from Database import MCT_DB
import re
class Forget_Pass:
    def __init__(self,app):
        #window app
        self.app=app
        self.mct=MCT_DB()
        self.show_password1 = False  # Track password visibility
        #Creating Frame
        self.frame=ctk.CTkFrame(
            self.app,
            fg_color="#FFFAFA"
        )
        #full frame Image settings
        Full_frame_Image = ImageTk.PhotoImage(Image.open("bg_im_fp.png").resize((500,800)))
        self.Full_frame = ctk.CTkFrame(
            self.app,
            fg_color="#FA99A3"
        )
        self.Full_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        label = ctk.CTkLabel(
            self.Full_frame,
            image=Full_frame_Image,
            text=""
        )
        label.place(relx=0, rely=0, relwidth=1, relheight=1)
        back_button_pic = ImageTk.PhotoImage(Image.open("back_button.png").resize((30, 30)))
        back_button = ctk.CTkButton(
            self.Full_frame,
            image=back_button_pic,
            text="",
            fg_color="#FA99A3",
            hover_color="#FECCCB",
            width=0,
            height=0,
            cursor="hand2",
            command=lambda: self.back_button_command()
        )
        back_button.place(x=55, y=35)
        # small frame in middle
        self.middle_frame=ctk.CTkFrame(
            self.Full_frame,
            fg_color="lightpink",
            width=280,
            height=220 ,
            corner_radius=8,
            border_width=2,
            border_color="black"
        )
        self.middle_frame.place(x=62, y=190)
        #Reset Password
        Reset_Label=ctk.CTkLabel(
            self.middle_frame,
            text="Reset Password",
            font=("Bahnschrift Light ", 20,"bold"),
            text_color="black"
        )
        Reset_Label.place(x=65,y=10)

        self.email_entry = ctk.CTkEntry(
            self.middle_frame,
            placeholder_text="Your Email",
            width=200,
            height=30,
            fg_color="white",
            border_color="black",
            corner_radius=10,
            border_width=1,
            text_color="black"
        )
        self.email_entry.place(x=45, y=50)
        self.New_password_entry = ctk.CTkEntry(
            self.middle_frame,
            placeholder_text="New Password",
            width=200,
            height=30,
            fg_color="white",
            corner_radius=10,
            border_color="black",
            border_width=1,
            text_color="black"

        )

        self.New_password_entry.place(x=45, y=90)
        #Reset Button
        Reset_but = ctk.CTkButton(
            self.middle_frame,
            text="Reset Password",
            corner_radius=10,
            height=35,
            width=200,
            fg_color="#B43D3A",
            font=("Bahnschrift Light ", 20, "bold"),
            text_color="black",
            hover_color="#FECCCB",
            command=lambda:self.changepass()

        )
        Reset_but.place(x=45, y=137)
        self.eye_closed = ImageTk.PhotoImage(Image.open("hide.png").resize((20, 20)))
        # Eye button for Password Entry
        self.toggle_button = ctk.CTkButton(
            self.middle_frame,
            image=self.eye_closed,
            text="",
            width=5, height=5,
            fg_color="white",
            hover_color="#E0E0E0",
            command=self.toggle_password1
        )
        self.toggle_button.place(
            in_=self.New_password_entry,
            relx=0.90,
            rely=0.5,
            anchor="center"
        )

    def toggle_password1(self):
        """Toggle visibility for Password field (entry2)."""
        self.show_password1 = not self.show_password1
        if self.show_password1:
            self.New_password_entry.configure(show="")  # Show password
            self.toggle_button.configure(image=self.eye_closed)
        else:
            self.New_password_entry.configure(show="●")  # Hide password
            self.toggle_button.configure(image=self.eye_closed)
    def is_valid_email(self, email):
        """Check if the email follows a valid pattern"""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

    def back_button_command(self):
        from Log_In import Login
        self.frame.destroy()
        self.Full_frame.destroy()
        Login(self.app)
    def changepass(self):
        get_email=self.email_entry.get()
        get_newpass=self.New_password_entry.get()
        # Check if email is valid
        if not self.is_valid_email(get_email):
            messagebox.showerror("Error", "Invalid email format. Please enter a correct email!")
            return
        if not get_newpass:
            messagebox.showerror("Error", "Please enter a new password!")
            return
        response=self.mct.Forgot_Password(get_email,get_newpass)
        labelreturn=ctk.CTkLabel(
            self.middle_frame,
            text=response,
            text_color="white",
            font=("Arial",9)
        )
        labelreturn.place(x=10,y=185)
