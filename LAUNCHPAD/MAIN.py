from EMPLOYEE import *
from tkinter import *

master = Tk()
master.title('Main Window')


def signup():
    employee()


signUp = Button(master, text='Sign Up',
                command=signup).pack(padx=100, pady=100)


master.mainloop()
