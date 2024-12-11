from tkinter import *
from tkinter import ttk
import mysql.connector as sqltor

class Conn:

    def close(self):
        print("Connection does not exist.")
        return None
    
    def cursor(self):
        return None

mycon = Conn()
mycur = mycon.cursor()
pwd = 'sqltime'

connected = False

def establish_connection():
    global mycur
    global mycon
    global connected
    try:
        mycon = sqltor.connect(user='root', host='localhost', password=pwd)
        mycur = mycon.cursor()
        print("Connection Established.")
        connected = True
    except Exception as e:
        print("Exception:", e)

def execute(*args):
    try:
        cmd = sqlcommand.get()
        mycur.execute(cmd)
    except ValueError:
        pass
    except Exception as e:
        print(e)


root = Tk()
root.title("MySQL GUI")

root.option_add('*tearOff', FALSE)

menubar = Menu(root)
root['menu'] = menubar

menu_mysql = Menu(menubar)
menubar.add_cascade(menu=menu_mysql, label='MySQL')

menu_mysql.add_command(label='Connect', command=establish_connection)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sqlcommand = StringVar()
cmd_entry = ttk.Entry(root, width=50, textvariable=sqlcommand)
cmd_entry.grid(column=0, row=0, rowspan=3, sticky=(W, E), padx=20, pady=30)

enter_button = ttk.Button(root, width=10, text="Execute", command=execute)
enter_button.grid(row=0, column=3, padx=20, pady=30)

cmd_entry.focus()
root.bind("<Return>", execute)

root.mainloop()
mycon.close()