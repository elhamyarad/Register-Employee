from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import UserInterfaceLayer.EmployeeFormModule

def mainFormLoad(firstName, lastName):
    mainForm = Tk()
    mainForm.title('MainForm')
    mainForm.geometry('400x400')
    mainForm.resizable(0, 0)
    mainForm.iconbitmap('images/mainForm.ico')
    right = int(mainForm.winfo_screenwidth() / 2 - 400 / 2)
    down = int(mainForm.winfo_screenheight() / 2 - 400 / 2)

    def employeeCRUDFunction():
        mainForm.destroy()
        UserInterfaceLayer.EmployeeFormModule.employeeFormLoad()

    mainForm.geometry('+{}+{}'.format(right, down))
    lblWelcomeMessage = ttk.Label(mainForm, text='Welcome ' + firstName + ' ' + lastName + '!')
    lblWelcomeMessage.grid(row=0, column=0, padx=20, pady=20, sticky='n')

    employeePhoto = PhotoImage(file='images/employeeForm.png')
    btnEmployeeCRUD = Button(mainForm, text='Employee CRUD',image=employeePhoto,compound=TOP,pady=10,
                             width=100, height=100, command=employeeCRUDFunction)

    btnEmployeeCRUD.grid(row=1, column=0, padx=20, pady=20, sticky='w')

    mainForm.mainloop()
