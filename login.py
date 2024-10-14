#!C:/Users/Tasnima Tabassum/AppData/Local/Programs/Python/Python39/python.exe
import mysql.connector
import cgi
from tkinter import *
from tkinter import messagebox

print("Content-Type:text/html")
print()

form = cgi.FieldStorage()
email = form.getvalue("email")
password = (form.getvalue("password"))

conn = mysql.connector.connect(host="localhost", user="books", password="books123", database="testone")
MyCursor = conn.cursor()
sql = "SELECT password FROM signupinfos where email = %s && password= %s "
MyCursor.execute(sql, (email, password,))
results = MyCursor.fetchone()
RowNum = MyCursor.rowcount

if RowNum == 1:
    print("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://127.0.0.1/bookshelf/home.html\">\n")
else:
    # message
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    # window.withdraw()
    
    messagebox.showwarning("Warning", "Invalid email or password!!", parent=window)
    window.deiconify()
    window.destroy()
    window.quit()
