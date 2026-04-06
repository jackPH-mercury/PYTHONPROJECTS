import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import calendar
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Tkinter Calendar")
        self.root.geometry("500x520")
        self.root.configure(bg="#1e1e2f")

        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self.today = datetime.now()

        self.appointments = {}  # {(year, month, day): ["event1", ...]}

        self.header = tk.Frame(root, bg="#1e1e2f")
        self.header.pack(pady=10)

        style = ttk.Style()
        style.theme_use('default')

        self.prev_btn = ttk.Button(self.header, text="◀", command=self.prev_month)
        self.prev_btn.grid(row=0, column=0)

        self.title_label = tk.Label(self.header, text="", font=("Segoe UI", 16, "bold"), fg="white", bg="#1e1e2f")
        self.title_label.grid(row=0, column=1, padx=20)

        self.next_btn = ttk.Button(self.header, text="▶", command=self.next_month)
        self.next_btn.grid(row=0, column=2)

        self.calendar_frame = tk.Frame(root, bg="#1e1e2f")
        self.calendar_frame.pack(pady=10)

        self.draw_calendar()

    def draw_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        self.title_label.config(text=f"{calendar.month_name[self.current_month]} {self.current_year}")

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            tk.Label(self.calendar_frame, text=day, font=("Segoe UI", 10, "bold"), fg="#00d4ff", bg="#1e1e2f", width=6).grid(row=0, column=i, pady=5)

        month_days = calendar.monthcalendar(self.current_year, self.current_month)

        for r, week in enumerate(month_days, start=1):
            for c, day in enumerate(week):
                if day == 0:
                    tk.Label(self.calendar_frame, text="", width=6, height=3, bg="#1e1e2f").grid(row=r, column=c)
                else:
                    date_key = (self.current_year, self.current_month, day)
                    is_today = (day == self.today.day and
                                self.current_month == self.today.month and
                                self.current_year == self.today.year)

                    bg_color = "#2a2a40"
                    fg_color = "white"

                    if is_today:
                        bg_color = "#00d4ff"
                        fg_color = "black"

                    if date_key in self.appointments:
                        bg_color = "#ff6b6b"

                    btn = tk.Button(self.calendar_frame,
                                    text=str(day),
                                    width=6,
                                    height=3,
                                    bg=bg_color,
                                    fg=fg_color,
                                    relief="flat",
                                    command=lambda d=day: self.handle_day_click(d))
                    btn.grid(row=r, column=c, padx=2, pady=2)

    def handle_day_click(self, day):
        date_key = (self.current_year, self.current_month, day)

        if date_key in self.appointments:
            events = self.appointments[date_key]
            event_text = "\n".join(f"• {e}" for e in events)

            choice = messagebox.askquestion(
                "Appointments",
                f"Appointments for {day}:\n\n{event_text}\n\nWould you like to add another?"
            )

            if choice == 'yes':
                self.add_appointment(day)
        else:
            self.add_appointment(day)

    def add_appointment(self, day):
        date_key = (self.current_year, self.current_month, day)
        event = simpledialog.askstring("Add Appointment", f"Enter appointment for {day}:")

        if event:
            if date_key not in self.appointments:
                self.appointments[date_key] = []
            self.appointments[date_key].append(event)

            messagebox.showinfo("Saved", f"Appointment added for {day}.")
            self.draw_calendar()

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.draw_calendar()

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.draw_calendar()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()