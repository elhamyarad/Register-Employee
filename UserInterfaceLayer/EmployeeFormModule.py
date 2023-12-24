from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
from tkcalendar import DateEntry
import UserInterfaceLayer.MainFormModule
from BusinessLogicLayer import UserBLLModule
from babel import dates
from babel import numbers


# Screen
def employeeFormLoad():
    employeeForm = Tk()
    employeeForm.geometry('400x400')
    employeeForm.title('Register Employee')
    employeeForm.iconbitmap('images/employee.ico')
    right = int(employeeForm.winfo_screenwidth() / 2 - 400 / 2)
    down = int(employeeForm.winfo_screenheight() / 2 - 400 / 2)
    employeeForm.geometry('+{}+{}'.format(right, down))

    def checkValidation():
        result = ''
        if len(txtFirstName.get()) > 20:
            result = result + 'FirstName Length Must Be 20 Character!'
        if len(txtLastName.get()) > 20:
            result = result + '\nLastName Length Must Be 20 Character!'
        if len(txtNationalCode.get()) > 10:
            result = result + '\nNationalCode Length Must Be 10 Character!'
        if len(txtJobTitle.get()) > 30:
            result = result + '\nJobTitle Length Must Be 30 Character!'
        return result

    def registerEmployee():
        result = checkValidation()
        if len(result) > 0:
            msg.showerror('Error', result)
        else:
            if intSex.get() == 1:
                Sex = 'Male'
            else:
                Sex = 'Female'
            params = (txtFirstName.get(), txtLastName.get(), txtNationalCode.get(), txtBirthdate.get(), Sex,
                      txtHiredate.get(), txtJobTitle.get(), txtDepartment.get()[0])
            connectionString2 = 'DB/pyadv.db'
            commandText2 = 'INSERT INTO Employee ' \
                           '(FirstName,LastName,NationalCode,BirthDate,Sex,HireDate,JobTitle,DepartmentID)' \
                           ' VALUES (?,?,?,?,?,?,?,?)'

            with sqlite3.Connection(connectionString2) as connection2:
                cursor2 = connection2.cursor()
                cursor2.execute(commandText2, params)
                connection2.commit()

            msg.showinfo('Congratulation!', 'Your registration is complete!')

    def resetForm():
        for widget in employeeForm.winfo_children():
            if type(widget) == ttk.Entry:
                widget.delete(0, END)
            if type(widget) == ttk.Combobox:
                txtDepartment.set(" ")
            if type(widget) == ttk.Radiobutton:
                intSex.set(0)

    # Lables

    lblFirstName = ttk.Label(employeeForm, text='FirstName: ')
    lblFirstName.grid(row=0, column=0, padx=10, pady=20, sticky='w')

    txtFirstName = StringVar()
    entFirstName = ttk.Entry(employeeForm, width=40, textvariable=txtFirstName)
    entFirstName.grid(row=0, column=1, padx=20, pady=20)

    lblLastName = ttk.Label(employeeForm, text='LastName: ')
    lblLastName.grid(row=1, column=0, padx=10, pady=0, sticky='w')

    txtLastName = StringVar()
    entLastName = ttk.Entry(employeeForm, width=40, textvariable=txtLastName)
    entLastName.grid(row=1, column=1, padx=20, pady=0)

    lblNationalCode = ttk.Label(employeeForm, text='NationalCode: ')
    lblNationalCode.grid(row=2, column=0, padx=10, pady=20, sticky='w')

    txtNationalCode = StringVar()
    entNationalCode = ttk.Entry(employeeForm, width=40, textvariable=txtNationalCode)
    entNationalCode.grid(row=2, column=1, padx=20, pady=20)

    lblBirthdate = ttk.Label(employeeForm, text='Birthdate: ')
    lblBirthdate.grid(row=3, column=0, padx=10, pady=0, sticky='w')

    txtBirthdate = StringVar()
    entBirthdate = DateEntry(employeeForm, width=36, textvariable=txtBirthdate)
    entBirthdate.grid(row=3, column=1, padx=20, pady=0)

    lblHiredate = ttk.Label(employeeForm, text='Hiredate: ')
    lblHiredate.grid(row=4, column=0, padx=10, pady=20, sticky='w')

    txtHiredate = StringVar()
    entHiredate = DateEntry(employeeForm, width=36, textvariable=txtHiredate)
    entHiredate.grid(row=4, column=1, padx=20, pady=20)

    lblSex = ttk.Label(employeeForm, text='Sex: ')
    lblSex.grid(row=5, column=0, padx=10, pady=0, sticky='w')

    intSex = IntVar()
    entSexMale = ttk.Radiobutton(employeeForm, width=20, text='Male', value=1, variable=intSex)
    entSexMale.grid(row=5, column=1, padx=20, pady=0, sticky='w')

    entSexFemale = ttk.Radiobutton(employeeForm, width=20, text='Female', value=2, variable=intSex)
    entSexFemale.grid(row=5, column=1, padx=20, pady=0, sticky='e')

    lblJobTitle = ttk.Label(employeeForm, text='JobTiTle: ')
    lblJobTitle.grid(row=6, column=0, padx=10, pady=20, sticky='w')

    txtJobTitle = StringVar()
    entJobTitle = ttk.Entry(employeeForm, width=40, textvariable=txtJobTitle)
    entJobTitle.grid(row=6, column=1, padx=20, pady=20)

    lblDepartment = ttk.Label(employeeForm, text='Department: ')
    lblDepartment.grid(row=7, column=0, padx=10, pady=0, sticky='w')

    txtDepartment = StringVar()

    connectionString = 'DB/pyadv.db'
    commandText = 'SELECT ID, DepartmentName FROM Department'
    with sqlite3.Connection(connectionString) as connection:
        cursor = connection.cursor()
        cursor.execute(commandText)
        rows = cursor.fetchall()

    departments = []
    for row in rows:
        departments.append(str(row[0]) + '-' + row[1])

    cmbDepartment = ttk.Combobox(employeeForm, width=36, textvariable=txtDepartment, values=departments,
                                 state='readonly')
    cmbDepartment.grid(row=7, column=1, padx=20, pady=0)

    btnReset = ttk.Button(employeeForm, text='Reset Form', width=16, command=resetForm)
    btnReset.grid(row=8, column=1, padx=20, pady=20, sticky='w')

    btnRegister = ttk.Button(employeeForm, text='Register Employee', width=20, command=registerEmployee)
    btnRegister.grid(row=8, column=1, padx=20, pady=20, sticky='e')

    # loading Form
    employeeForm.mainloop()
