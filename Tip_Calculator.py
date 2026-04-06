import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar

# ================= FUNCTION =================
def update_calculation(*args):
    """
    Recalculate tip, total, and per-person amount whenever input changes.
    Handles invalid input gracefully.
    """
    try:
        bill = float(bill_var.get())
        tip_percent = int(tip_var.get())
        people = int(people_var.get())

        if bill < 0:
            raise ValueError

        tip_amount = bill * (tip_percent / 100)
        total = bill + tip_amount
        per_person = total / people

        tip_result.set(f"${tip_amount:.2f}")
        total_result.set(f"${total:.2f}")
        per_person_result.set(f"${per_person:.2f}")

    except:
        # If invalid input, show placeholder values
        tip_result.set("--")
        total_result.set("--")
        per_person_result.set("--")


def clear_fields():
    """Reset all input fields to default values."""
    bill_var.set("")
    tip_var.set("15")
    people_var.set("1")


# ================= WINDOW =================
app = ttk.Window(themename="superhero")
app.title("Modern Tip Calculator")
app.geometry("400x420")

# ✅ Allow resizing
app.resizable(True, True)

# Make the main window responsive
app.columnconfigure(0, weight=1)

# ================= VARIABLES =================
bill_var = StringVar()
tip_var = StringVar(value="15")
people_var = StringVar(value="1")

tip_result = StringVar(value="$0.00")
total_result = StringVar(value="$0.00")
per_person_result = StringVar(value="$0.00")

# ================= TITLE =================
ttk.Label(app, text="💰 Tip Calculator", font=("Helvetica", 20, "bold"))\
    .pack(pady=15, fill=X)

# ================= BILL INPUT =================
frame_bill = ttk.Frame(app, padding=10)
frame_bill.pack(fill=X, expand=True)

ttk.Label(frame_bill, text="Bill Amount").pack(anchor=W)
ttk.Entry(frame_bill, textvariable=bill_var, bootstyle="info")\
    .pack(fill=X, expand=True, pady=5)

# ================= TIP SELECTION =================
frame_tip = ttk.Frame(app, padding=10)
frame_tip.pack(fill=X, expand=True)

ttk.Label(frame_tip, text="Tip Percentage").pack(anchor=W)

tip_buttons = ttk.Frame(frame_tip)
tip_buttons.pack()

for percent in ["10", "15", "20"]:
    ttk.Radiobutton(
        tip_buttons,
        text=f"{percent}%",
        variable=tip_var,
        value=percent,
        bootstyle="success"   # ✅ fixed (no outline)
    ).pack(side=LEFT, padx=5, pady=5)

# ================= PEOPLE =================
frame_people = ttk.Frame(app, padding=10)
frame_people.pack(fill=X, expand=True)

ttk.Label(frame_people, text="Number of Diners").pack(anchor=W)
ttk.Spinbox(
    frame_people,
    from_=1,   # ✅ fixed (no negative diners)
    to=6,
    textvariable=people_var,
    bootstyle="warning"
).pack(fill=X, expand=True, pady=5)

# ================= RESULTS =================
frame_results = ttk.Frame(app, padding=15)
frame_results.pack(fill=BOTH, expand=True)

# Make result columns expand nicely
frame_results.columnconfigure(0, weight=1)
frame_results.columnconfigure(1, weight=1)

ttk.Label(frame_results, text="Tip").grid(row=0, column=0, sticky=W)
ttk.Label(frame_results, textvariable=tip_result, font=("Helvetica", 12, "bold"))\
    .grid(row=0, column=1, sticky=E)

ttk.Label(frame_results, text="Total").grid(row=1, column=0, sticky=W)
ttk.Label(frame_results, textvariable=total_result, font=("Helvetica", 12, "bold"))\
    .grid(row=1, column=1, sticky=E)

ttk.Label(frame_results, text="Per Person").grid(row=2, column=0, sticky=W)
ttk.Label(frame_results, textvariable=per_person_result, font=("Helvetica", 14, "bold"))\
    .grid(row=2, column=1, sticky=E)

# ================= BUTTONS =================
btn_frame = ttk.Frame(app, padding=10)
btn_frame.pack()

ttk.Button(btn_frame, text="Clear", command=clear_fields, bootstyle="secondary")\
    .pack(side=LEFT, padx=10)

ttk.Button(btn_frame, text="Exit", command=app.quit, bootstyle="danger")\
    .pack(side=LEFT, padx=10)

# ================= AUTO UPDATE =================
bill_var.trace_add("write", update_calculation)
tip_var.trace_add("write", update_calculation)
people_var.trace_add("write", update_calculation)

# Run application
app.mainloop()