from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from BusinessLogicLayer import UserBLLModule
from UserInterfaceLayer import MainFormModule

# Screen
loginForm = Tk()
loginForm.title('LoginForm')
loginForm.geometry('400x160')
loginForm.resizable(0, 0)
loginForm.iconbitmap('images/login.ico')
right = int(loginForm.winfo_screenwidth() / 2 - 400 / 2)
down = int(loginForm.winfo_screenheight() / 2 - 160 / 2)
loginForm.geometry('+{}+{}'.format(right, down))

# region Functions ...
def loginFunction():
    username = txtUserName.get()
    password = txtPassword.get()

    if username != "" and password != "":
        row = UserBLLModule.loginFunction(username, password)
        if row is not None:
            firstName, lastName = row[2], row[3]
            loginForm.destroy()
            MainFormModule.mainFormLoad(firstName, lastName)
        else:
            msg.showinfo('Error', 'UserName or Password is incorrect!!!')


def checkValidation(*args):
    if len(txtUserName.get()) > 20:
        txtUserName.set(txtUserName.get()[:20])
    if len(txtPassword.get()) > 20:
        txtPassword.set(txtPassword.get()[:20])
    if not txtUserName.get().isalpha():
        txtUserName.set(txtUserName.get()[:len(txtUserName.get())-1])

# endregion


# Lables
lblUserName = Label(loginForm, text='UserName:')
lblUserName.grid(row=0, column=0, padx=10, pady=10)

lblPassword = Label(loginForm, text='Password:')
lblPassword.grid(row=1, column=0, padx=10, pady=10)

# Entry
txtUserName = StringVar()
txtUserName.trace('w', checkValidation)
entUserName = ttk.Entry(loginForm, width=40, textvariable=txtUserName)
entUserName.grid(row=0, column=1, padx=10, pady=15)

txtPassword = StringVar()
txtPassword.trace('w', checkValidation)
entPassword = ttk.Entry(loginForm, width=40, show='*', textvariable=txtPassword)
entPassword.grid(row=1, column=1, padx=10, pady=10)

btnLogin = ttk.Button(loginForm, text='Login', width=20, command=loginFunction)
btnLogin.grid(row=2, column=1, padx=10, pady=20, sticky='e')

# loading Form
loginForm.mainloop()
