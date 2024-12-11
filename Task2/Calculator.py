import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="#1E1E1E")  
root.resizable(width=False, height=False)

ent_field = tk.Entry(
    root,
    bg="#2D2D2D",
    fg="#FFFFFF",
    font=("Arial", 30),
    borderwidth=5,
    justify="right",
    insertbackground="#FFFFFF"
)
ent_field.grid(row=0, columnspan=8, padx=10, pady=20, sticky="nsew")
ent_field.insert(0, "0")

FONT = ("Arial", 12, "bold")
BUTTON_COLOR = "#333333"
TEXT_COLOR = "#FFFFFF"
HIGHLIGHT_COLOR = "#FF5722"

class SC_Calculator():
    def __init__(self):
        self.current = ''
        self.inp_value = True
        self.result = False

    def Entry(self, value):
        ent_field.delete(0, "end")
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum + secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == "=":
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str + val)
            self.inp_value = False
        except (ValueError, SyntaxError):
            self.Entry("Error")

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

    def SQ_Root(self):
        try:
            self.current = math.sqrt(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry("Error")

    def Pi(self):
        self.result = False
        self.current = math.pi
        self.Entry(self.current)

    def E(self):
        self.result = False
        self.current = math.e
        self.Entry(self.current)

    def Deg(self):
        try:
            self.result = False
            self.current = math.degrees(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry("Error")

    def Rad(self):
        try:
            self.result = False
            self.current = math.radians(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry("Error")

    def Exp(self):
        try:
            self.result = False
            self.current = math.exp(float(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry("Error")

    def Fact(self):
        try:
            self.result = False
            self.current = math.factorial(int(ent_field.get()))
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry("Error")

    def Trig(self, func):
        try:
            angle = math.radians(float(ent_field.get()))
            self.current = func(angle)
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry("Error")

    def Log(self, base):
        try:
            self.current = math.log(float(ent_field.get()), base)
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry("Error")

    def Pow(self, power):
        try:
            self.current = float(ent_field.get()) ** power
            self.Entry(self.current)
        except (ValueError, SyntaxError):
            self.Entry("Error")


sc_app = SC_Calculator()

def create_button(text, row, col, command, color=BUTTON_COLOR):
    return tk.Button(
        root,
        text=text,
        command=command,
        font=FONT,
        width=5,
        height=2,
        fg=TEXT_COLOR,
        bg=color,
        activebackground=HIGHLIGHT_COLOR,
        activeforeground=TEXT_COLOR,
        highlightbackground=BUTTON_COLOR,
        highlightthickness=2
    ).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(8):
    root.grid_columnconfigure(j, weight=1)

buttons = [
    ("CE", 1, 0, lambda: sc_app.Clear_Entry()),
    ("\u221A", 1, 1, lambda: sc_app.SQ_Root()),
    ("\u03C0", 1, 2, lambda: sc_app.Pi()),
    ("e", 1, 3, lambda: sc_app.E()),
    ("+", 1, 4, lambda: sc_app.Standard_Ops("+")),
    ("-", 1, 5, lambda: sc_app.Standard_Ops("-")),
    ("*", 1, 6, lambda: sc_app.Standard_Ops("*")),
    ("/", 1, 7, lambda: sc_app.Standard_Ops("/")),
    ("7", 2, 0, lambda: sc_app.Enter_Num(7)),
    ("8", 2, 1, lambda: sc_app.Enter_Num(8)),
    ("9", 2, 2, lambda: sc_app.Enter_Num(9)),
    ("sin", 2, 3, lambda: sc_app.Trig(math.sin)),
    ("cos", 2, 4, lambda: sc_app.Trig(math.cos)),
    ("tan", 2, 5, lambda: sc_app.Trig(math.tan)),
    ("4", 3, 0, lambda: sc_app.Enter_Num(4)),
    ("5", 3, 1, lambda: sc_app.Enter_Num(5)),
    ("6", 3, 2, lambda: sc_app.Enter_Num(6)),
    ("ln", 3, 3, lambda: sc_app.Log(math.e)),
    ("log10", 3, 4, lambda: sc_app.Log(10)),
    ("log2", 3, 5, lambda: sc_app.Log(2)),
    ("1", 4, 0, lambda: sc_app.Enter_Num(1)),
    ("2", 4, 1, lambda: sc_app.Enter_Num(2)),
    ("3", 4, 2, lambda: sc_app.Enter_Num(3)),
    ("x^2", 4, 3, lambda: sc_app.Pow(2)),
    ("x^3", 4, 4, lambda: sc_app.Pow(3)),
    ("1/x", 4, 5, lambda: sc_app.Pow(-1)),
    ("0", 5, 0, lambda: sc_app.Enter_Num(0)),
    (".", 5, 1, lambda: sc_app.Standard_Ops(".")),
    ("=", 5, 2, lambda: sc_app.Standard_Ops("="), HIGHLIGHT_COLOR),
    ("!", 5, 3, lambda: sc_app.Fact()),
    ("Rad", 5, 4, lambda: sc_app.Rad()),
    ("Deg", 5, 5, lambda: sc_app.Deg()),
]

for text, row, col, cmd, *args in buttons:
    create_button(text, row, col, cmd, *args)

root.mainloop()
