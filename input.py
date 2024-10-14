#!C:/Users/Tasnima Tabassum/AppData/Local/Programs/Python/Python39/python.exe
import mysql.connector
import cgi
import os
print("Content-Type:text/html")
print()


form = cgi.FieldStorage()

Name = form.getvalue("book_name")
Price = form.getvalue("book_price")
Writer = form.getvalue("book_writer")
Mobile = form.getvalue("mobile_no")
Category = form.getvalue("book_category")


fle = form['image']
fn = os.path.basename(fle.filename)
filename = fle.filename
open("D:/xampp/htdocs/bookshelf/uploadedImages/" + fn, "wb").write(fle.file.read())

conn = mysql.connector.connect(host="localhost", user="books", password="books123", database="testone")
myCursor = conn.cursor()


sql = "INSERT INTO userinput(bookName, bookPrice, bookWriter, mobileNo, bookCategory, bookImage) VALUES (%s, %s, %s, %s, %s, %s)"
value = (Name, Price, Writer, Mobile, Category, filename, )
sql = myCursor.execute(sql, value)
conn.commit()
myCursor.close()
conn.close()
# print(Name, Price, Writer, Category, filename)
print("<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://127.0.0.1/bookshelf/home.html\">\n")


