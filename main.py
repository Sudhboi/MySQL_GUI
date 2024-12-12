from tkinter import *
from tkinter import ttk
import mysql.connector as sqltor
from tkinter import messagebox

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
debugging = True

def show_connection_box():

    def establish_connection(*args):
        global mycur
        global mycon
        global connected
        try:
            mycon = sqltor.connect(user=uservar.get(), host=hostvar.get(), password=passvar.get() if not debugging else 'sqltime')
            mycur = mycon.cursor()
            connected = True
            messagebox.showinfo(message='Connection Established Successfully')
            enter_button.state(['!disabled'])
            cbox.destroy()
        except Exception as e:
            messagebox.showinfo(message="Exception: " + str(e))

    cbox = Toplevel(root)

    frame = ttk.Frame(cbox, padding="3 3 12 12")
    frame.grid()

    host_Label = ttk.Label(frame, text='Enter Host:')
    host_Label.grid(row=0, column=0, columnspan=2)

    hostvar = StringVar()
    hostvar.set('localhost')
    host_Entry = ttk.Entry(frame, width=20, textvariable=hostvar)
    host_Entry.grid(row=0, column=2)

    user_Label = ttk.Label(frame, text='Enter User:')
    user_Label.grid(row=1, column=0, columnspan=2)

    uservar = StringVar()
    uservar.set("root")
    user_Entry = ttk.Entry(frame, width=20, textvariable=uservar)
    user_Entry.grid(row=1, column=2)

    pass_Label = ttk.Label(frame, text='Enter Password:')
    pass_Label.grid(row=2, column=0, columnspan=2)

    passvar = StringVar()
    pass_Entry = ttk.Entry(frame, width=20, textvariable=passvar)
    pass_Entry.grid(row=2, column=2)

    cbutton = ttk.Button(frame, text='Connect', command=establish_connection)
    cbutton.grid(row=1, column=3)

    for child in cbox.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

def execute(*args):
    try:
        cmd = sqlcommand.get()
        mycur.execute(cmd)
        data = mycur.fetchall()
        rowcount.set("Command Executed Successfully. Current Cursor Row Count - " + str(mycur.rowcount))        
    except ValueError:
        pass
    except Exception as e:
        messagebox.showinfo(message="Exception: " + str(e))
        rowcount.set("Command Resulted in Error.")


root = Tk()
root.title("MySQL GUI")
root.option_add('*tearOff', FALSE)

menubar = Menu(root)
root['menu'] = menubar

menu_mysql = Menu(menubar)
menubar.add_cascade(menu=menu_mysql, label='MySQL')

menu_mysql.add_command(label='Connect', command=show_connection_box)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

s1 = ttk.Separator(mainframe, orient="horizontal").grid(row=0, column=0, columnspan=4, sticky=(E, W))

input_Frame = ttk.Labelframe(mainframe, text='Input')
input_Frame.grid(row=1, column=0, columnspan=4, sticky=(N, W, E, S), padx=10, pady=10)

mysql_label = ttk.Label(input_Frame, text='mysql>')
mysql_label.grid(row=1, column=0, padx=5)

sqlcommand = StringVar()
cmd_entry = ttk.Entry(input_Frame, width=50, textvariable=sqlcommand)
cmd_entry.grid(row=1, column=1, columnspan=2, sticky=(W, E), padx=5, pady=5)

enter_button = ttk.Button(input_Frame, width=10, text="Execute", command=execute)
enter_button.grid(row=1, column=3, padx=5, pady=5)
enter_button.state(['disabled'])

s2 = ttk.Separator(mainframe, orient="horizontal").grid(row=2, column=0, columnspan=4, sticky=(E, W))

output_Frame = ttk.Labelframe(mainframe, text='Output')
output_Frame.grid(row=3, column=0, rowspan=4, columnspan=4, padx=10, pady=10,sticky=(N, W, E, S))

rowcount = StringVar()
rowcount.set("No Command Executed.")
rowcount_Label = ttk.Label(output_Frame, textvariable=rowcount)
rowcount_Label.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

cmd_entry.focus()
root.bind("<Return>", execute)

root.mainloop()
mycon.close()