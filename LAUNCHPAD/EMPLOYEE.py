from tkinter import *
from tkinter.messagebox import *
from mysql.connector import *
from tkcalendar import DateEntry
from SERIAL import *
root = Tk()
root.title('Employees')

# database connection
conn = connect(
    host='localhost',
    user='root',
    password='Huzefalegend786',
    database='employeedb'
)
cur = conn.cursor()

# functions

# reservation


def save():
    ser = str(serial)
    first_name = e_first_name.get().title()
    last_name = e_last_name.get().title()
    date = date_.get()
    from_ = e_from_.get().title()
    username = e_username.get()
    password = e_password.get()
    if first_name == '' or last_name == '' or date == '' or from_ == '' or username == '' or password == '':
        showinfo('Employee Status', 'All Fields Required!!')
    else:
        cur.execute('select * from employee where Username="' + username+'"')
        records = cur.fetchall()
        if records == [] and len(password) >= 8:
            cur.execute('insert into employee(Serial, First_Name, Last_Name, Date_Of_Birth, From_, Username, Password) values("'+ser+'","'+first_name+'","' +
                        last_name+'","'+date+'","'+from_+'","'+username+'","'+password+'")')
            cur.execute('commit')

            e_first_name.delete(0, END)
            e_last_name.delete(0, END)
            e_from_.delete(0, END)
            e_username.delete(0, END)
            e_password.delete(0, END)
            showinfo('Employee Status',
                     'Employee Successful \n Serial='+str(ser))
        elif records == [] and len(password) < 8:
            showinfo('Employee Status',
                     'Password Must Be 8 Or More Characters')
        else:
            showinfo('Employee Status', 'Username Taken')


# Entry
e_username = Entry(root, width=30)
e_username.grid(row=1, column=1, padx=20, pady=(0, 5))
e_first_name = Entry(root, width=30)
e_first_name.grid(row=3, column=1, padx=20, pady=(0, 5))
e_last_name = Entry(root, width=30)
e_last_name.grid(row=4, column=1, padx=20, pady=(0, 5))
# date entry
date_ = StringVar()
e_date = DateEntry(root, selectmode='month', textvariable=date_)
e_date.grid(row=5, column=1, padx=20, pady=(0, 5))

e_from_ = Entry(root, width=30)
e_from_.grid(row=6, column=1, padx=20, pady=(0, 5))
e_password = Entry(root, width=30, show='*')
e_password.grid(row=9, column=1, padx=20, pady=(0, 5))


# labels
title_label = Label(root, text='Employees', font=('bold', 20))
title_label.grid(row=0, column=0, padx=20, pady=(0, 5), columnspan=2)

username_label = Label(root, text='Username:')
username_label.grid(row=1, column=0, padx=20, pady=(0, 5))
first_name_label = Label(root, text='First Name:')
first_name_label.grid(row=3, column=0, padx=20, pady=(0, 5))
last_name_label = Label(root, text='Last Name:')
last_name_label.grid(row=4, column=0, padx=20, pady=(0, 5))
date_label = Label(root, text='Date:')
date_label.grid(row=5, column=0, padx=20, pady=(0, 5))
from_label = Label(root, text='From:')
from_label.grid(row=6, column=0, padx=20, pady=(0, 5))
password_label = Label(root, text='Password:')
password_label.grid(row=9, column=0, padx=20, pady=(0, 5))

# buttons
employee = Button(root, text='Save', command=save)
employee.grid(row=10, column=0, padx=20, pady=(0, 5), columnspan=2)

root.mainloop()
