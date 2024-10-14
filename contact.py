#!C:/Users/Tasnima Tabassum/AppData/Local/Programs/Python/Python39/python.exe
import mysql.connector
import cgi
from tkinter import *
from tkinter import messagebox
print("Content-Type:text/html")
print()

form = cgi.FieldStorage()
uname = form.getvalue("userName")
uemail = form.getvalue("userEmail")
umessage = form.getvalue("userMessage")

conn = mysql.connector.connect(host="localhost", user="books", password="books123", database="testone")
myCursor = conn.cursor()

sql = "INSERT INTO contact(uname,uemail,umessage) VALUES(%s,%s,%s)"
values = (uname, uemail, umessage, )
myCursor.execute(sql, values)
conn.commit()
myCursor.close()
conn.close()
print("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://127.0.0.1/bookshelf/home.html\">\n")
