import _tkinter
import mysql.connector as sqltor

class Conn:
    def close(self):
        print("Connection does not exist.")
        return None

mycon = Conn()

pwd = input("Enter Password: ")

try:
    mycon = sqltor.connect(user='root', host='localhost', password=pwd)
except Exception as e:
    print("Exception:", e)

mycon.close()