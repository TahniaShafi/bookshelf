#!C:/Users/Tasnima Tabassum/AppData/Local/Programs/Python/Python39/python.exe
import mysql.connector
import cgi
from tkinter import *
from tkinter import messagebox
print("Content-Type:text/html")
print()

form = cgi.FieldStorage()
email = form.getvalue("email")
password = form.getvalue("password")
terms = form.getvalue("terms")

conn = mysql.connector.connect(host="localhost", user="books", password="books123", database="testone")
myCursor = conn.cursor()

checkExisting = "SELECT * FROM signupinfos WHERE email= %s"
value = (email, )
checkingQuery = myCursor.execute(checkExisting, value)
result = myCursor.fetchone()

if myCursor.rowcount == 1:
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    # window.withdraw()

    messagebox.showwarning("Warning", "Another account with this email exists!!", parent=window)
    window.deiconify()
    window.destroy()
    window.quit()
    print("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://127.0.0.1/bookshelf/signup.html\">\n")

else:
    sql = "INSERT INTO signupinfos(email,password) VALUES(%s,%s)"
    values = (email, password)
    myCursor.execute(sql, values)
    conn.commit()
    myCursor.close()
    conn.close()

    print("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://127.0.0.1/bookshelf/login.html\">\n")
