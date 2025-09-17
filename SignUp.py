import customtkinter as ctk
from PIL import Image,ImageTk
from First_Page import FirstPage
from Database import MCT_DB
from tkinter import messagebox
from tkinter import StringVar, IntVar

import re
class Sign_UP:
    def __init__(self,app):
        self.app=app
        self.show_password1 = False  # Track password visibility

        self.mct=MCT_DB()
        self.frame = ctk.CTkFrame(self.app,
            fg_color="#DC6E87")
        self.frame.pack(fill="both", expand=True)
        back_button_pic = ImageTk.PhotoImage(Image.open("back_button.png").resize((30, 30)))
        back_button = ctk.CTkButton(
            self.frame,
            image=back_button_pic,
            text="",
            fg_color="#DC6E87",
            hover_color="#FECCCB",
            width=0,
            height=0,
            cursor="hand2",
            command=lambda: self.back_button_command()
        )
        back_button.place(x=25, y=15)

        label = ctk.CTkLabel(self.frame,
             text_color="white",
             text="Register\n Create your Account",
             font=("Bahnschrift Light ", 25),
             fg_color="transparent",height=0,width=0
        )
        label.place(x=85, y=30)
        self.name_entry = ctk.CTkEntry(self.frame,
             placeholder_text="Username",
             width=260,
             height=40,
             fg_color="white",
             corner_radius=12,
             border_color="black",
             border_width=1,
             text_color="black"
        )
        self.name_entry.place(x=65, y=100)
        self.email_entry = ctk.CTkEntry(self.frame,
                                        placeholder_text="Your Email",
                                        width=260,
                                        height=40,
                                        fg_color="white",
                                        border_color="black",
                                        corner_radius=12,
                                        border_width=1,
                                        text_color="black"
                                        )
        self.email_entry.place(x=65, y=146)
        self.password_entry = ctk.CTkEntry(self.frame,
                                           placeholder_text="Password",
                                           width=260,
                                           height=40,
                                           fg_color="white",
                                           corner_radius=12,
                                           border_color="black",
                                           border_width=1,
                                           text_color="black"

                                           )
        self.password_entry.place(x=65, y=193)

        self.Age_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Enter Your Age",
            width=260,
            height=40,
            fg_color="white",
            corner_radius=12,
            border_color="black",
            border_width=1,
            text_color="black"
        )
        self.Age_entry.place(x=65, y=240)
        self.Weight_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Enter Your Weight in kilograms",
            width=260,
            height=40,
            fg_color="white",
            corner_radius=12,
            border_color="black",
            border_width=1,
            text_color="black"
        )
        self.Weight_entry.place(anchor="w", x=65, y=308)
        self.Height_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Enter Your Height in cm",
            width=260,
            height=40,
            fg_color="white",
            corner_radius=12,
            border_color="black",
            border_width=1,
            text_color="black"
        )
        self.Height_entry.place(anchor="w", x=65, y=356)
        MaritalLabel = ctk.CTkLabel(
            self.frame,
            text="Marital Status:",
            font=("Bahnschrift Light ", 14, "bold"),
            text_color="white"
        )
        MaritalLabel.place(x=65, y=390)
        self.Marital_status = StringVar(value="Single")
        self.radio_single = ctk.CTkRadioButton(
            self.frame,
            text="Single",
            text_color="white",
            font=("Bahnschrift Light ", 12, "bold"),
            variable=self.Marital_status,
            value="Single",
            border_color="#B43D3A",
            hover_color="black",
            fg_color="#B43D3A",
        )
        self.radio_single.place(x=175, y=395)
        self.radio_single = ctk.CTkRadioButton(
            self.frame,
            text="Married",
            text_color="white",
            font=("Bahnschrift Light ", 12, "bold"),
            variable=self.Marital_status,
            value="Married",
            border_color="#B43D3A",
            hover_color="black",
            fg_color="#B43D3A"
        )
        self.radio_single.place(x=260, y=395)
        SignUp = ctk.CTkButton(self.frame,
            text="SIGN UP ",
            corner_radius=10,
            height=40,
            width=260,
            fg_color="#B43D3A",
            font=("Bahnschrift Light ", 20, "bold"),
            text_color="white",
            hover_color="#FECCCB",
            command=lambda:self.Signup_user()
        )
        SignUp.place(x=65, y=440)
        LoginIn_link = ctk.CTkLabel(
            self.frame,
            text="Already have an account?",
            font=("Bahnschrift Light ", 14, "underline"),
            text_color="white",
            fg_color="#DC6E87"
        )
        LoginIn_link.place(x=85, y=503)
        # Login_button
        Login_button = ctk.CTkButton(
            self.frame,
            text="Login",
            font=("Bahnschrift Light ", 14, "underline"),
            cursor="hand2",
            text_color="white",
            fg_color="#DC6E87",
            width=0,
            height=0,
            hover_color="#B43D3A",
            command=lambda:self.Login()
        )
        Login_button.place(x=260, y=505)
        self.eye_closed = ImageTk.PhotoImage(Image.open("hide.png").resize((20, 20)))
        # Eye button for Password Entry
        self.toggle_button = ctk.CTkButton(
            self.frame,
            image=self.eye_closed,
            text="",
            width=0, height=0,
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
        else:
            self.password_entry.configure(show="●")  # Hide password

    def back_button_command(self):
        self.frame.destroy()
        FirstPage(self.app)
    def Login(self):
        from Log_In import Login
        self.frame.destroy()
        Login(self.app)
    def is_valid_email(self, email):
        """Check if the email follows a valid pattern"""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

    def Signup_user(self):
        try:
            self.get_name = self.name_entry.get().strip()
            self.get_age=self.Age_entry.get()
            self.get_weight=self.Weight_entry.get()
            self.get_height=self.Height_entry.get()
            self.get_password = self.password_entry.get().strip()
            self.get_email = self.email_entry.get().strip()
            self.get_marital_status = self.Marital_status.get()
            if not all(
                    [self.get_name,
                     self.get_age,
                     self.get_weight,
                     self.get_height,
                     self.get_password,
                     self.get_email,
                     self.get_marital_status
                     ]
            ):
                messagebox.showerror("Error", "All fields are required. Please fill in all fields.")
                return
        except ValueError:
            messagebox.showerror("Error", "Age must be an integer. Weight and Height must be decimal numbers.")
            return
        # Check if email is valid
        if not self.is_valid_email(self.get_email):
            messagebox.showerror("Error", "Invalid email format. Please enter a correct email!")
            return  # Stop
        response=self.mct.sign_up_database(
            self.get_name,
            self.get_email,
            self.get_password,
            self.get_age,
            self.get_weight,
            self.get_height,
            self.get_marital_status
        )
        self.label_successful = None
        if self.label_successful:
            self.label_successful.destroy()
        label_successful=ctk.CTkLabel(
            self.frame,
            text=response,
            text_color="white",
            font=("Bahnschrift Light",9,"bold")
            )
        label_successful.place(x=10,y=480)
