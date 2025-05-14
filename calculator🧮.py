import customtkinter as ctk
from simpleeval import simple_eval

# Set appearance and scaling
ctk.set_appearance_mode("dark")  # OLED black background
ctk.set_default_color_theme("dark-blue")  # Optional theme

# Create window
window = ctk.CTk()
window.geometry("300x300")
window.title("Calculator")

calculation = ""

def add_to_field(value):
    global calculation
    calculation += str(value)
    field.delete(1.0, "end")
    field.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        result = simple_eval(calculation)
        field.delete(1.0, "end")
        field.insert(1.0, str(result))
        calculation = str(result)
    except:
        field.delete(1.0, "end")
        field.insert(1.0, "Error")
        calculation = ""

def clear():
    global calculation
    calculation = ""
    field.delete(1.0, "end")

# Entry display
field = ctk.CTkTextbox(window, height=80, width=340, font=("Arial", 28), text_color="white", 
    bg_color="#000000", fg_color="#1C1C1C", corner_radius=10)
field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button config
buttons = [
    ("AC", 1, 0, lambda: clear(), "#D4D4D2", "black"),
    ("/", 1, 1, lambda: add_to_field("/"), "#FF9500", "white"),
    ("*", 1, 2, lambda: add_to_field("*"), "#FF9500", "white"),
    ("-", 1, 3, lambda: add_to_field("-"), "#FF9500", "white"),

    ("7", 2, 0, lambda: add_to_field("7"), "#1C1C1C", "white"),
    ("8", 2, 1, lambda: add_to_field("8"), "#1C1C1C", "white"),
    ("9", 2, 2, lambda: add_to_field("9"), "#1C1C1C", "white"),
    ("+", 2, 3, lambda: add_to_field("+"), "#FF9500", "white"),

    ("4", 3, 0, lambda: add_to_field("4"), "#1C1C1C", "white"),
    ("5", 3, 1, lambda: add_to_field("5"), "#1C1C1C", "white"),
    ("6", 3, 2, lambda: add_to_field("6"), "#1C1C1C", "white"),
    ("=", 3, 3, lambda: evaluate(), "#FF9500", "white"),

    ("1", 4, 0, lambda: add_to_field("1"), "#1C1C1C", "white"),
    ("2", 4, 1, lambda: add_to_field("2"), "#1C1C1C", "white"),
    ("3", 4, 2, lambda: add_to_field("3"), "#1C1C1C", "white"),
    (".", 4, 3, lambda: add_to_field("."), "#1C1C1C", "white"),

    ("0", 5, 0, lambda: add_to_field("0"), "#1C1C1C", "white"),
]

# Create buttons with border radius
for (text, row, col, cmd, bg_color, fg_color) in buttons:
    btn = ctk.CTkButton(window, text=text, command=cmd, fg_color=bg_color, text_color=fg_color,
                        font=("Arial", 20), width=80, height=60, corner_radius=15)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Make column span for "0" button (like on iPhones)
for c in range(4):
    window.grid_columnconfigure(c, weight=1)
for r in range(7):
    window.grid_rowconfigure(r, weight = 1)


window.mainloop()
