import calendar
import customtkinter as ctk
from datetime import datetime, timedelta
from PIL import Image
import numpy as np
import torch
import joblib
from model_lstm import PeriodLSTM
from config import url, key
from supabase import create_client

class PeriodTracker(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.configure(fg_color="white")
        self.current_year = datetime.today().year
        self.current_month = datetime.today().month
        self.selected_dates = []
        self.skipped_months = []
        self.selected_labels = []
        self.period_length = 5  # default

        self.lstm_model = PeriodLSTM(5, 64, 1)
        self.lstm_model.load_state_dict(torch.load("period_lstm_model.pth"))
        self.lstm_model.eval()
        self.scaler = joblib.load("scaler.pkl")
        self.Client = create_client(url, key)

        self.setup_ui()

    def setup_ui(self):
        self.app.title("Periodoc")
        self.app.geometry("400x600")
        self.app.configure(fg_color="white")
        self.pack(fill="both", expand=True)

        self.create_header()
        self.create_calendar_section()
        self.create_period_dropdown()
        self.create_labels_section()

    def create_header(self):
        header = ctk.CTkFrame(self, fg_color="white", height=40)
        header.pack(fill="x", padx=10, pady=(10, 5))
        header.grid_columnconfigure(1, weight=1)

        bell_icon = ctk.CTkImage(light_image=Image.open("bellicon.jpeg"), size=(24, 24))
        back_icon = ctk.CTkImage(Image.open("back_button.png"), size=(24, 24))

        back_button = ctk.CTkButton(header, image=back_icon, text="", fg_color="transparent",
                                    hover_color="#FFC0CB", width=36, height=36, corner_radius=8,
                                    command=self.back_button_command)
        back_button.grid(row=0, column=0, sticky="w")

        title_label = ctk.CTkLabel(header, text="Periodoc", font=("Helvetica", 20, "bold"),
                                   text_color="#D64C7F")
        title_label.grid(row=0, column=1, sticky="w", padx=10)

        bell_button = ctk.CTkButton(header, text="", image=bell_icon, fg_color="transparent",
                                    hover_color="#FFC0CB", width=36, height=36, corner_radius=8,
                                    command=self.on_bell_click)
        bell_button.grid(row=0, column=2, sticky="e")

    def create_calendar_section(self):
        self.month_label = ctk.CTkLabel(self, text="", font=("Constantia", 14), text_color="black")
        self.month_label.pack(pady=(5, 0))

        self.box = ctk.CTkFrame(self, fg_color="white")
        self.box.pack(pady=5)

        self.create_navigation_buttons()
        self.update_month_label()
        self.display_calendar()

    def create_navigation_buttons(self):
        frame = ctk.CTkFrame(self, fg_color="white", width=250, height=40)
        frame.pack(pady=10)

        ctk.CTkButton(frame, text="PREVIOUS", text_color="white", command=lambda: self.change_month(-1),
                      fg_color="#ba6578", hover_color="#DC6E87", width=80, font=('Poppins', 11, "bold")).place(x=0, y=0)

        self.skip_button = ctk.CTkButton(frame, text="SKIP", text_color="white", command=self.skip_current_month,
                                         fg_color="#ba6578", hover_color="#DC6E87", width=80,
                                         font=('Poppins', 11, "bold"))
        self.skip_button.place(x=85, y=0)

        ctk.CTkButton(frame, text="NEXT", text_color="white", command=lambda: self.change_month(1),
                      fg_color="#ba6578", hover_color="#DC6E87", width=80, font=('Poppins', 11, "bold")).place(x=170, y=0)

    def create_period_dropdown(self):
        settings_frame = ctk.CTkFrame(self, fg_color="#FDF6F4", corner_radius=10)
        settings_frame.pack(fill="x", padx=20, pady=(0, 10))

        row = ctk.CTkFrame(settings_frame, fg_color="transparent")
        row.pack(fill="x", padx=15, pady=10)

        label = ctk.CTkLabel(row, text="Period Length (days):", font=("Helvetica", 14, "bold"), text_color="#333333")
        label.pack(side="left")

        self.period_combo = ctk.CTkComboBox(row, values=["1", "2", "3", "4", "5", "6", "7", "More"],
                                            font=("Helvetica", 14), width=100,
                                            command=self.set_period_length)
        self.period_combo.set("5")
        self.period_combo.pack(side="right")

    def set_period_length(self, choice):
        try:
            self.period_length = int(choice)
        except:
            self.period_length = 5

    def create_labels_section(self):
        y_start, x_pos = 10, 100
        for i in range(4):
            lbl = ctk.CTkLabel(self, text=f"Selected Date {i + 1}: None",
                               font=("Bahnschrift Light Condensed", 12), text_color="black")
            lbl.pack(anchor="w", padx=40)
            self.selected_labels.append(lbl)

        self.next_period_label = ctk.CTkLabel(self, text="Next Period (AI): Select 4 dates",
                                              font=("Bahnschrift", 14, "bold"), text_color="black")
        self.next_period_label.pack(anchor="w", padx=40, pady=(10, 10))

    def display_calendar(self):
        for widget in self.box.winfo_children():
            widget.destroy()

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for col, day in enumerate(days):
            label = ctk.CTkLabel(self.box, text=day, font=("Constantia", 10), text_color="black", width=5)
            label.grid(row=0, column=col)

        cal = calendar.monthcalendar(self.current_year, self.current_month)
        for row, week in enumerate(cal, start=1):
            for col, day in enumerate(week):
                if day == 0:
                    continue
                color = "pink" if datetime(self.current_year, self.current_month, day) in self.selected_dates else "white"
                button = ctk.CTkButton(self.box, text=str(day), font=("Arial", 10), width=5,
                                       fg_color=color, text_color="black", hover_color="pink",
                                       command=lambda d=day: self.select_date(d))
                button.grid(row=row, column=col)

    def select_date(self, day):
        selected = datetime(self.current_year, self.current_month, day)
        if selected in self.selected_dates:
            self.selected_dates.remove(selected)
        elif len(self.selected_dates) + len(self.skipped_months) < 4:
            self.selected_dates.append(selected)
        else:
            print("Limit reached: 4 entries")
            return

        self.selected_dates.sort()
        self.update_selected_labels()
        self.display_calendar()
        self.predict_next_period_with_lstm()

    def update_selected_labels(self):
        combined = [(d, "selected") for d in self.selected_dates] + [
            (datetime(y, m, 1), "skipped") for (y, m) in self.skipped_months]
        combined.sort(key=lambda x: x[0])

        for i in range(4):
            if i < len(combined):
                dt, status = combined[i]
                label = f"Skipped ({dt.strftime('%b %Y')})" if status == "skipped" else dt.strftime("%b %d, %Y")
                self.selected_labels[i].configure(text=f"Selected Date {i + 1}: {label}")
            else:
                self.selected_labels[i].configure(text=f"Selected Date {i + 1}: None")

        if len(self.selected_dates) + len(self.skipped_months) >= 4:
            self.skip_button.configure(state="disabled")
        else:
            self.skip_button.configure(state="normal")

    def prepare_lstm_input(self):
        if len(self.selected_dates) < 4:
            return None

        self.selected_dates.sort()
        sequence = []
        for i in range(3):
            cycle = (self.selected_dates[i + 1] - self.selected_dates[i]).days
            sequence.append([cycle, 14, 14, self.period_length, 10])

        scaled = self.scaler.transform(np.array(sequence)).reshape(1, 3, 5)
        return torch.tensor(scaled, dtype=torch.float32)

    def predict_next_period_with_lstm(self):
        input_tensor = self.prepare_lstm_input()
        if input_tensor is None:
            self.next_period_label.configure(text="Next Period (AI): Select 4 dates")
            return

        with torch.no_grad():
            predicted_cycle = self.lstm_model(input_tensor).item()

        predicted_days = round(predicted_cycle)
        latest_date = max(self.selected_dates)
        next_period = latest_date + timedelta(days=predicted_days)

        self.next_period_label.configure(
            text=f"Next Period (AI): {next_period.strftime('%b %d, %Y')} (Len: {predicted_days} days)"
        )

    def skip_current_month(self):
        month_year = (self.current_year, self.current_month)
        if month_year not in self.skipped_months:
            self.skipped_months.append(month_year)
            self.update_selected_labels()
            self.change_month(1)

    def change_month(self, direction):
        if direction == -1:
            self.current_year, self.current_month = self.get_previous_month(self.current_year, self.current_month)
        else:
            self.current_year, self.current_month = self.get_next_month(self.current_year, self.current_month)
        self.update_month_label()
        self.display_calendar()

    def update_month_label(self):
        self.month_label.configure(text=f"{calendar.month_name[self.current_month]} {self.current_year}")

    def get_next_month(self, year, month):
        return (year + 1, 1) if month == 12 else (year, month + 1)

    def get_previous_month(self, year, month):
        return (year - 1, 12) if month == 1 else (year, month - 1)

    def on_bell_click(self):
        print("🔔 Bell clicked!")

    def back_button_command(self):
        for widget in self.app.winfo_children():
            widget.destroy()
        from insights import Insights
        Insights(self.app)
