import os
import google.generativeai as genai
import warnings
import time
from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter as tk


class PeriodBotApp:
    def __init__(self, app):
        # Suppress warnings
        self.app = app
        warnings.filterwarnings('ignore')
        # Gemini API Configuration
        genai.configure(api_key="AIzaSyDTH2D3f-v__jQjdWEEihzCXSicCjYix2A")
        generation_config = {
            "temperature": 0.35,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            generation_config=generation_config,
            system_instruction="dont give answer anything unrelated remember you are a period bot onlyy give solutions/remedies according to symptoms user is facing also give every answer related to periods or mood swings like as if condittion( i am sayin g im so irritated you shouldnt consider it any other problem tyou must consider that its must be because of me harmonal changes or my periods) so relate every problem with this dont go out of topic\nim saying again and againnn dont give tooooo much longgg responsess yeah give the  points or remedies but try to be short",
        )

        self.chat_session = self.model.start_chat(
            history=[
                {"role": "user", "parts": [
                    "You are a virtual health consultant focusing on period-related issues. Provide advice and remedies."]},
                {"role": "model", "parts": [
                    "Okay, I understand. I'm ready to act as your virtual health consultant specializing in menstrual-related issues."]}
            ]
        )

        # Build UI

        self.app = app
        self.app.title("Period Tracker Bot")

        # Colors and Styles
        primary_color = "#FFC0CB"  # Pink
        secondary_color = "#FFFFFF"  # White
        user_msg_color = "#FFB6C1"  # Light Pink
        bot_msg_color = "#FFFFFF"  # White
        text_color = "#333333"

        # Header Frame
        header_frame = ctk.CTkFrame(self.app, fg_color=primary_color, corner_radius=15)
        header_frame.pack(fill="x", padx=20, pady=(10, 0))

        # Back Button
        back_button_pic = ImageTk.PhotoImage(Image.open("back_button.png").resize((30, 30)))
        back_button = ctk.CTkButton(
            header_frame,  # change here!
            image=back_button_pic,
            text="",
            fg_color="#DC6E87",
            hover_color="#FECCCB",
            width=40,  # thoda width height do for better click area
            height=40,
            cursor="hand2",
            command=lambda: self.back_button_command()
        )
        back_button.pack(side="left", padx=(5, 0), pady=5)

        # Header Label
        header_label = ctk.CTkLabel(
            header_frame,
            text="Period Tracker Bot",
            text_color="white",
            font=("Arial", 18, "bold")
        )
        header_label.pack(side="left", expand=True, pady=5)

        # Chat Frame
        chat_frame = ctk.CTkFrame(self.app, fg_color=secondary_color, corner_radius=15)
        chat_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Canvas for Scrollable Messages
        self.canvas = tk.Canvas(chat_frame, bg=secondary_color, highlightthickness=0)
        scrollbar = ctk.CTkScrollbar(chat_frame, command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=secondary_color)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # User Input Entry
        self.user_input = ctk.CTkEntry(self.app, placeholder_text="Type your message...", fg_color=secondary_color,
                                       text_color=text_color, corner_radius=10)
        self.user_input.pack(padx=20, pady=(0, 10), fill="x")

        # Send Button
        send_button = ctk.CTkButton(self.app, text="Send", command=self.send_message, fg_color=primary_color,
                                    text_color="white", hover_color="#EE8292", corner_radius=10)
        send_button.pack(padx=20, pady=(0, 20), fill="x")

        self.primary_color = primary_color
        self.user_msg_color = user_msg_color
        self.bot_msg_color = bot_msg_color
        self.text_color = text_color

    def send_message(self):
        message = self.user_input.get()
        if message:
            # Display User Message
            user_msg_box = ctk.CTkFrame(self.scrollable_frame, fg_color=self.user_msg_color, corner_radius=15)
            user_msg_label = ctk.CTkLabel(user_msg_box, text=message, text_color=self.text_color, wraplength=250,
                                          justify="left")
            user_msg_label.pack(padx=10, pady=5)
            user_msg_box.pack(anchor="e", padx=10, pady=5, fill="x", expand=False)

            # Get response from Gemini API
            response = self.chat_session.send_message(message)
            reply = response.text if hasattr(response, 'text') else response.candidates[0].text

            # Display Bot Message
            bot_msg_box = ctk.CTkFrame(self.scrollable_frame, fg_color=self.bot_msg_color, corner_radius=15)
            bot_msg_label = ctk.CTkLabel(bot_msg_box, text=reply, text_color=self.text_color, wraplength=250,
                                         justify="left")
            bot_msg_label.pack(padx=10, pady=5)
            bot_msg_box.pack(anchor="w", padx=10, pady=5, fill="x", expand=False)

            # Clear input field and scroll to the bottom
            self.user_input.delete(0, "end")
            self.canvas.update_idletasks()
            self.canvas.yview_moveto(1.0)

    def send_mood_prompt(self, mood):
        # Mood ke hisab se fixed prompts
        prompts = {
            "Happy": "I'm feeling happy during my period. Suggest 1 quick activity to boost my mood in one line.",
            "Sad": "I'm feeling sad due to PMS. Give me 1 comforting tip in one line.",
            "Angry": "I'm very irritable before my period. Recommend 1 quick calming technique in one line."
        }

        # User input box mein prompt daalo aur send karo
        self.user_input.delete(0, "end")  # Clear old text
        self.user_input.insert(0, prompts[mood])  # Auto-fill prompt
        self.send_message()  # Existing send function call

    def back_button_command(self):
        from insights import Insights
        # Clear current UI instead of destroying the whole window
        for widget in self.app.winfo_children():
            widget.destroy()
        Insights(self.app)