import customtkinter as ctk
from PIL import Image,ImageTk
from First_Page import FirstPage
from tkinter import messagebox
from Database import MCT_DB
import re
class Login:
    def __init__(self,app):
        self.app=app
        self.mct=MCT_DB()
        self.show_password1 = False  # Track password visibility
        self.frame = ctk.CTkFrame(
            self.app,
            fg_color="#FFFAFA"
        )
        self.frame.pack(fill="both", expand=True)
        #Setting upper frame image
        self.upper_frame_img = ImageTk.PhotoImage(Image.open("Images_used\half_bg_image.jpg").resize((600,475)))
        self.frame2 = ctk.CTkFrame(self.app, fg_color="#DC6E87")
        self.frame2.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        self.label = ctk.CTkLabel(
            self.frame2,
            image=self.upper_frame_img,
            text=""
        )
        self.label.place(relx=0, rely=0, relwidth=1, relheight=1)
        # Welcome Label
        label = ctk.CTkLabel(
            self.frame,
            text="Welcome Back!",
            font=("Arial", 25, "bold"),
            text_color= "#bd425e"
        )
        label.place(x=115, y=325)
        # Back Button
        back_button_pic = ImageTk.PhotoImage(Image.open("back_button.png").resize((30,30)))
        back_button = ctk.CTkButton(
            self.frame2,
            image = back_button_pic,
            text = "",
            fg_color="white",
            hover_color="#FFFFFF",
            width=0,
            height=0,
            cursor="hand2",
            command = lambda : self.back_button_command()
        )
        back_button.place(x=25, y=25)

        # Email Icon
        email_icon = ImageTk.PhotoImage(Image.open("email.jpg").resize((50, 40)))
        self.email_icon_label = ctk.CTkLabel(
            self.frame,
            image = email_icon,
            text = ""
        )
        self.email_icon_label.place(x = 40, y = 372)
        self.email_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Your Email",
            width=260,
            height=40,
            fg_color="white",
            border_color="black",
            border_width=1,
            text_color="black"
        )
        self.email_entry.place(anchor="w", x=85, y=390)
        #Password Icon
        password_icon = ImageTk.PhotoImage(Image.open("pass.jpg").resize((50, 40)))
        password_icon_label = ctk.CTkLabel(
            self.frame,
            image=password_icon,
            text = ""
        )
        password_icon_label.place(x = 40, y = 423)
        self.password_entry  = ctk.CTkEntry(
            self.frame,
            placeholder_text="Password",
            width=260,
            height=40,
            fg_color="white",
            border_color="black",
            border_width=1,
            text_color="black"
        )
        self.password_entry .place(anchor="w", x=85, y=440)
        # Forgot Password Label
        forgot_password_label = ctk.CTkButton(
            self.frame,
            text="Forgot Password?",
            font=("Arial", 12),
            text_color="#2f477f",
            fg_color="transparent",
            width=0,
            height=0,
            hover_color="#FFFAFA",
            cursor="hand2",
            command=lambda: self.forgot_password()
        )
        forgot_password_label.place(x=240, y=465)

        LogIn = ctk.CTkButton(
            self.frame,
            text="Log In",
            corner_radius=8,
            height=40,
            width=260,
            hover_color="#bd425e",
            fg_color="#EE8292",
            font=("Bahnschrift Light Condensed", 20, "bold"),
            text_color="white",
            cursor = "hand2",
            command=lambda: self.login()
        )
        LogIn.place(x=85, y=490)
        #Signup Link
        signup_link = ctk.CTkLabel(
            self.frame,
            text="Don't have an account?",
            font=("Bahnschrift Light Condensed", 14, "underline"),
            text_color="#DC6E87"
        )
        signup_link.place( x=132, y=550)
        #Signup Button
        signup_button = ctk.CTkButton(
            self.frame,
            text = "Sign Up",
            font=("Bahnschrift Light Condensed", 14, "underline"),
            text_color="#DC6E87",
            cursor="hand2",
            width = 0,
            height = 0,
            fg_color = "#FFFAFA",
            hover_color = "#FFFAFA",
            command = lambda: self.signup()
        )
        signup_button.place(x=245, y=552)
        self.eye_closed = ImageTk.PhotoImage(Image.open("hide.png").resize((20, 20)))
        # Eye button for Password Entry
        self.toggle_button = ctk.CTkButton(
            self.frame,
            image=self.eye_closed,
            text="",
            width=30, height=30,
            fg_color="white",
            hover_color="#E0E0E0",
            command=self.toggle_password1
        )
        self.toggle_button.place(
            in_=self.password_entry,
            relx=0.90,
            rely=0.5,
            anchor="center"
        )
    def toggle_password1(self):
        """Toggle visibility for Password field (entry2)."""
        self.show_password1 = not self.show_password1
        if self.show_password1:
            self.password_entry.configure(show="")  # Show password
            self.toggle_button.configure(image=self.eye_closed)
        else:
            self.password_entry.configure(show="●")  # Hide password
            self.toggle_button.configure(image=self.eye_closed)

    # Signup Button Comamnd
    def signup(self):
        from SignUp import Sign_UP
        self.frame.destroy()
        self.frame2.destroy()
        Sign_UP(self.app)

    def is_valid_email(self, email):
        """Check if the email follows a valid pattern"""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)
    # Login Button Command
    def login(self):
        get_email = self.email_entry.get().strip()
        get_password = self.password_entry.get().strip()

        # Check if email is valid
        if not self.is_valid_email(get_email):
            messagebox.showerror("Error", "Invalid email format. Please enter a correct email!")
            return

        # Check credentials from the database
        response = self.mct.Log_In_database(get_email, get_password)
        message_text = response["message"]

        if response["status"] == "success":
            # Login successful
            messagebox.showinfo("Info", message_text)
            self.frame.destroy()
            self.frame2.destroy()
            from insights import Insights
            Insights(self.app)
        else:
            # Login failed
            messagebox.showerror("Login Failed", message_text)

            """if hasattr(self, 'labellogin'):
                self.labellogin.destroy()  # Remove old label before adding new one

            labellogin=ctk.CTkLabel(
               self.frame,
               text=message_text,
               font=("Bahnschrift Light",10),
               text_color="#FFFAFA"
             )
            labellogin.place(x=20,y=530)"""

    # Forgot Pass Command
    def forgot_password(self):
        from Forgot_Password import Forget_Pass
        self.frame.destroy()
        self.frame2.destroy()

        Forget_Pass(self.app)
    def back_button_command(self):
        self.frame.destroy()
        self.frame2.destroy()
        FirstPage(self.app)

