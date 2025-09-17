import customtkinter as ctk
from PIL import Image, ImageTk
import webbrowser
class Insights:
    def __init__(self, app):
        self.app = app

        # Main Frame
        self.frame = ctk.CTkFrame(self.app, fg_color="#EE8292", width=450, height=150, corner_radius=15)
        self.frame.pack(padx=25, pady=20)
        self.frame.pack_propagate(False)
        # Icon Label
        icon_label = ctk.CTkLabel(self.frame, text_color="black", text="🩸", font=("Arial", 15))
        icon_label.pack(pady=(2, 2))
        # Average Cycle Length Title
        ctk.CTkLabel(self.frame, text_color="black", text="Average Cycle Length",
                     font=("Times New Roman", 20), anchor="center").pack(pady=(6, 5))
        # Frame to hold "28 days" on the same line
        self.length_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.length_frame.pack(pady=(5, 6))
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
        # Large "28" Label
        ctk.CTkLabel(self.length_frame, text="28", text_color="black",
                     font=("Times New Roman", 35, "bold")).pack(side="left")
        # Small "days" Label
        ctk.CTkLabel(self.length_frame, text="days", text_color="black",
                     font=("Times New Roman", 15)).pack(side="left", padx=(5, 0))  # Smaller font
        # Feelings Label
        self.feeling_label = ctk.CTkLabel(self.app, text="How are you feeling today?",
                                          font=("Times New Roman", 20, "bold"))
        self.feeling_label.pack(pady=(0, 5))

        self.feelings()
        self.insights()
        self.discovered()
        # ... rest of your __init__ method
        pass

    def feelings(self):
        moods = [("happy.png", "Happy"), ("sad.png", "Sad"), ("angry.png", "Angry")]
        self.mood_frame = ctk.CTkFrame(self.app, fg_color="transparent")  # Row container
        self.mood_frame.pack(pady=(2, 2))
        for i, (path, mood) in enumerate(moods):

            img = ctk.CTkImage(Image.open(path), size=(35, 35))  # Load image
            btn = ctk.CTkButton(
                self.mood_frame,
                text="",
                image=img,
                width=35,
                height=35,
                fg_color="transparent",
                hover_color="#EE8292",
                command=lambda m=mood: self.open_bot_with_mood(m)
            )
            btn.grid(row=0, column=i, padx=10)  # Place in grid row
            lbl = ctk.CTkLabel(self.mood_frame, text=mood)
            lbl.grid(row=1, column=i, pady=2)

    def open_bot_with_mood(self, mood):
        from bot2 import PeriodBotApp
        # Destroy current widgets
        for widget in self.app.winfo_children():
            widget.destroy()

        # Initialize the chatbot
        bot = PeriodBotApp(self.app)

        # Call the mood-based prompt sender
        bot.send_mood_prompt(mood)

    def insights(self):
        self.cycle_history_label = ctk.CTkLabel(self.app, text="Cycle History", font=("Times New Roman", 20, "bold"),
                                                anchor="w")
        self.cycle_history_label.pack(pady=(0, 5), padx=10)
        self.history_frame = ctk.CTkFrame(self.app, fg_color="transparent")  # Row container
        self.history_frame.pack()
        self.listt = ["Periods", "Cycle_Phase", "ChatBot"]
        for i in range(3):
            self.insightframe = ctk.CTkButton(self.history_frame, text="", hover_color="#F2D7E6", fg_color="#F2D7E6",
                                              width=90, height=90,
                                              command=lambda num=i: self.button_click_event(num))
            self.insightframe.pack(side="left", padx=5, pady=5)  # Using pack instead of grid
            self.insightframe.pack_propagate(False)  # Prevents shrinking
            try:
                img = ctk.CTkImage(Image.open("blood icon.png"), size=(35, 35))
                img_label = ctk.CTkLabel(self.insightframe, text="", image=img)
                img_label.pack(pady=(5, 0))  # Adjusted padding
                text_label = ctk.CTkLabel(self.insightframe, text=self.listt[i], font=("Arial", 12, "bold"))
                text_label.pack(pady=(0, 5))  # Text below image
            except FileNotFoundError:
                print("Error: blood_icon.png not found!")

    import webbrowser

    def discovered(self):
        self.discover_label = ctk.CTkLabel(self.app, text="Discover", font=("Times New Roman", 20, "bold"))
        self.discover_label.pack(pady=(0, 5))
        self.discover_frame = ctk.CTkFrame(self.app, fg_color="transparent")  # Row container
        self.discover_frame.pack()

        textt = ["Keep your\n Cycle Regular", "Exercise Body\n Yoga", "Learn about\n Best Diet"]

        # Links for articles and video
        links = [
            {"type": "article",
             "url": "https://www.healthline.com/health/womens-health/irregular-periods-home-remedies"},
            {"type": "video", "url": "https://www.youtube.com/watch?v=5JvbjrLESPs"},
            {"type": "article", "url": "https://www.healthline.com/nutrition/healthy-eating-tips"}
        ]

        for i in range(3):
            self.disframe = ctk.CTkFrame(self.discover_frame, border_color="#AACBDE", border_width=2,
                                         fg_color="transparent", width=100, height=100)
            self.disframe.grid(row=0, column=i, padx=5, pady=5)
            self.disframe.pack_propagate(False)

            ctk.CTkLabel(self.disframe, text=textt[i], font=("Times New Roman", 12, "bold")).pack(pady=5)

            # Set button text based on type (Article or Video)
            button_text = "Article" if links[i]["type"] == "article" else "Video"
            button_color = "#AACBDE" if button_text == "Article" else "#EE8292"

            ctk.CTkButton(self.disframe, text=button_text, font=("Arial Rounded MT Bold", 12),
                          width=50, height=20, corner_radius=5, fg_color=button_color,
                          command=lambda link=links[i]["url"]: self.open_link(link)).pack(pady=3)

    def open_link(self, link):
        webbrowser.open(link)  # Opens the given link in a web browser

    def back_button_command(self):
        for widget in self.app.winfo_children():
            widget.destroy()
        from Log_In import Login
        Login(self.app)

    def button_click_event(self, num):
        print(f"Button {self.listt[num]} clicked.")
        for widget in self.app.winfo_children():
            widget.destroy()
        if num == 0:
            from tracker import PeriodTracker
            PeriodTracker(self.app)  # Add parent frame if needed
        elif num == 1:
            from Phase_calculation import PhaseCalculatorPage
            PhaseCalculatorPage(self.app)
        elif num == 2:
            from bot2 import PeriodBotApp
            PeriodBotApp(self.app)
