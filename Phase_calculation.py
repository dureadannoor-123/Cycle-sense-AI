import customtkinter as ctk
from datetime import datetime, timedelta

# Dummy PeriodTracker example - replace with your actual PeriodTracker logic
class DummyPeriodTracker:
    def get_last_period_start_date(self):
        # Example: return a fixed last period start date
        return datetime(2025, 5, 1)

    def get_cycle_length(self):
        # Example average cycle length (days)
        return 28

    def get_period_length(self):
        # Example period length (days)
        return 7


class PhaseCalculatorPage:
    def __init__(self, app):
        self.app = app

        # Initialize period_tracker internally (replace DummyPeriodTracker with your real one)
        self.period_tracker = DummyPeriodTracker()

        # Current user info if needed (optional)
        self.current_user = None

        # Clear previous widgets
        for widget in self.app.winfo_children():
            widget.destroy()

        # Setup UI
        self.frame = ctk.CTkFrame(self.app, fg_color="#F8D7DA", width=400, height=300, corner_radius=15)
        self.frame.pack(padx=20, pady=20)
        self.frame.pack_propagate(False)

        self.title_label = ctk.CTkLabel(self.frame, text="Cycle Phase Calculator", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        # Label for displaying phase info
        self.phase_info_label = ctk.CTkLabel(self.frame, text="", font=("Arial", 16))
        self.phase_info_label.pack(pady=20)

        # Display current phase info
        self.display_phase_info()

        # Back button to go back to insights or main page
        self.back_button = ctk.CTkButton(self.frame, text="Back", command=self.go_back)
        self.back_button.pack(pady=10)

    def display_phase_info(self):
        try:
            phase, day_in_cycle = self.calculate_current_phase()
            info_text = f"Current phase: {phase}\nDay in cycle: {day_in_cycle}"
        except Exception as e:
            info_text = f"Error calculating phase:\n{str(e)}"
        self.phase_info_label.configure(text=info_text)

    def calculate_current_phase(self):
        last_period_start = self.period_tracker.get_last_period_start_date()
        cycle_length = self.period_tracker.get_cycle_length()
        period_length = self.period_tracker.get_period_length()

        today = datetime.now()
        days_since_period = (today - last_period_start).days % cycle_length

        # Define phases based on days since period start
        if days_since_period < period_length:
            phase = "Menstrual Phase"
        elif days_since_period < period_length + 6:
            phase = "Follicular Phase"
        elif days_since_period < cycle_length - 14:
            phase = "Ovulation Phase"
        else:
            phase = "Luteal Phase"

        return phase, days_since_period + 1  # +1 so day count starts at 1

    def go_back(self):
        # Clear this frame and go back to previous screen
        for widget in self.app.winfo_children():
            widget.destroy()
        from insights import Insights  # Adjust import based on your project structure
        Insights(self.app)
