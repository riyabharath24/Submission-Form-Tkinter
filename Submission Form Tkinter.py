import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("PythonGuides")
root.geometry("400x350")


def callback():
    print("The form has been submitted")


label1 = tk.Label(root, text="Full Name", font=("bold", 10), width=20)
label1.place(x=20, y=2)

e1 = tk.Entry(root, width=30)
e1.place(x=140, y=2)

label2 = tk.Label(root, text="Email", width=20, font=("bold", 10))
label2.place(x=20, y=32)

e1 = tk.Entry(root, width=30)
e1.place(x=140, y=32)

label3 = tk.Label(root, text="Password", width=20, font=("bold", 10))
label3.place(x=20, y=62)

e3 = tk.Entry(root, width=30)
e3.place(x=140, y=62)

label4 = Label(root, text="Gender", width=10, font=("bold", 10))
label4.place(x=45, y=92)


value = IntVar()
rb1 = tk.Radiobutton(root, text="Female", variable=value,
                     width=30, value=1).place(x=50, y=125)

rb2 = tk.Radiobutton(root, text="Male", variable=value,
                     width=30, value=2).place(x=45, y=155)

rb3 = tk.Radiobutton(root, text="Others", variable=value,
                     width=30, value=3).place(x=50, y=185)


chb = tk.Checkbutton(
    root, text="Accept the terms & conditions", width=50).place(x=20, y=235)
button = tk.Button(root, text="Submit", width=30,
                   command=callback).place(x=100, y=260)


root.mainloop()
