from tkinter import *
from tkinter import ttk
from sympy import *
import sympy as sp
from tkinter import messagebox

root = Tk()
root.title('the Newton-Raphson Method')

# Set the geometry of the window (width x height + x_offset + y_offset)
root.geometry("500x300+300+200")


lab = Label(root, text="Enter a function!\n f(x) =")
lab.pack()

entry = ttk.Entry(root, width=40)
entry.pack()


lab = Label(root, text="Enter an initial guess of x")
lab.pack()

entry2 = ttk.Entry(root, width=40)
entry2.pack()

button = ttk.Button(root, text="Submit")
button.pack()


def newton_method(f, x_):
    x = sp.Symbol('x')
    f_prime = sp.diff(f, x)

    # to be able to evaluate the function at specific x:
    f = lambdify(x, f)

    if f(x_) == 0:
        y = f"The answer is x = {x_}"
        messagebox.showinfo("Answer", y)
        return

    # to be able to evaluate the derivative of the function for a specific x:
    f_prime = lambdify(x, f_prime)

    # the main code of applying Newton-Raphson method:
    for i in range(1000000):
        if f_prime(x_) == 0:
            x = f"Can not apply Newton-Raphson method for this function!"
            messagebox.showinfo("Answer", x)
            return

        x_ = x_ - f(x_) / f_prime(x_)

    z = f"The answer is x = {x_}"
    messagebox.showinfo("Answer", z)


def submit():
    try:
        f = sp.sympify(entry.get())
    except sp.SympifyError:
        messagebox.showerror("Error", "Invalid function expression")
        return

    try:
        x_0 = float(entry2.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid initial guess")
        return

    newton_method(f, x_0)


button.config(command=submit)
root.mainloop()