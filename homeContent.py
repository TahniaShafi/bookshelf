import webbrowser

import mysql.connector
import cgi

print("Content-Type:text/html")
print()


serial = 0

conn = mysql.connector.connect(host="localhost", user="books", password="books123", database="testone")
Sql = "SELECT * FROM userInput ORDER BY id desc "
myCursor = conn.cursor()
myCursor.execute(Sql)
results = myCursor.fetchall()

# print(results)

while serial == 0:
    serial1name = results[serial][1]
    serial1price = results[serial][2]
    serial1writer = results[serial][3]
    serial1Mobile = results[serial][4]
    serial1category = results[serial][5]
    serial1image = results[serial][6]
    print(results[serial])
    serial += 1

while serial == 1:
    serial2name = results[serial][1]
    serial2price = results[serial][2]
    serial2writer = results[serial][3]
    serial2category = results[serial][5]
    serial2image = results[serial][6]
    # print(results[serial])
    serial += 1

while serial == 2:
    serial3name = results[serial][1]
    serial3price = results[serial][2]
    serial3writer = results[serial][3]
    serial3category = results[serial][5]
    serial3image = results[serial][6]
    # print(results[serial])
    serial += 1

while serial == 3:
    serial4name = results[serial][1]
    serial4price = results[serial][2]
    serial4writer = results[serial][3]
    serial4category = results[serial][5]
    serial4image = results[serial][6]
    # print(results[serial])
    serial += 1

while serial == 4:
    serial5name = results[serial][1]
    serial5price = results[serial][2]
    serial5writer = results[serial][3]
    serial5category = results[serial][5]
    serial5image = results[serial][6]
    # print(results[serial])
    break

html_content = f"<html>" \
               f"<head> <link rel='stylesheet' href='css/home.css'> <link href='https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&display=swap' rel='stylesheet'> <link href='https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap' rel='stylesheet'> </head>" \
               f"<body><div class='nav'>" \
               f"<div class='nav_heading'><h1>BOOKSHELF</h1></div>" \
               f"<div class='links'> " \
               f"<a href='#about_us'>About Us</a>" \
               f"<a href='#footer'>Contact</a>" \
               f"<a href='login.html'>Login</a>" \
               f"<a href='input.html'>Sell Book</a><input type='text' placeholder='Search Book'>" \
               f"</div></div>" \
               f"<div class='heading_part'><div class='body_heading'><h1>Bookshelf</h1> " \
               f"<p>Buy Your Favourite Books</P>" \
               f"<p>Sell Books You Have Read</p> <button class='heading_sell_book_button'><a href='input.html'>Sell Book</a></button>"\
               f"</div></div><div class='about_us' id='about_us'>" \
               f"<div class='about_heading'><h1>WHY US?</h1></div>" \
               f"<div class='about_info'><div class='about_para'><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur reprehenderit perspiciatis, deleniti repellendus hic nisi, earum minus, enim officia suscipit accusamus. Eos dolor illum voluptas perspiciatis porro recusandae ipsa voluptatem, saepe perferendis sed doloremque nam est deleniti minima cumque id non possimus, tempore quidem! Voluptatem porro ex cumque deserunt necessitatibus. Esse deleniti architecto beatae atque, qui repudiandae adipisci, distinctio debitis natus velit est quia? Atque id eum voluptas assumenda a alias, dolores eius porro modi adipisci, quasi provident ab dolore fugiat ratione neque vero ipsum deserunt accusantium non aut repellendus repellat. Voluptatum explicabo, corrupti reprehenderit laborum asperiores natus. Iste ipsam sapiente, tempore alias consectetur dolorem eligendi molestias officia illo accusantium illum vel quod autem fuga. Sit quae, perferendis odio ducimus ea accusantium quas! Corrupti error, sed explicabo quidem minus aliquam aspernatur assumenda doloremque ex eos ullam nulla!</p>" \
               f"</div><div class='about_image'><img src='./images/booklong.jpg'></div></div></div>" \
               f"<div class='container'>" \
               f"<div class='book_info'><div class='book_image'><img src='./uploadedImages/{serial1image}'></div><h1>{serial1name}</h1><p>By {serial1writer}</p><h4>{serial1price} Tk</h4><button class='buy_button'>See Details</button></div>" \
               f"<div class='book_info'><div class='book_image'><img src='./uploadedImages/{serial2image}'></div><h1>{serial2name}</h1><p>By {serial2writer}</p><h4>{serial2price} Tk</h4><button class='buy_button'>See Details</button></div>" \
               f"<div class='book_info'><div class='book_image'><img src='./uploadedImages/{serial3image}'></div><h1>{serial3name}</h1><p>By {serial3writer}</p><h4>{serial3price} Tk</h4><button class='buy_button'>See Details</button></div>" \
               f"<div class='book_info'><div class='book_image'><img src='./uploadedImages/{serial4image}'></div><h1>{serial4name}</h1><p>By {serial4writer}</p><h4>{serial4price} Tk</h4><button class='buy_button'>See Details</button></div>" \
               f"<div class='book_info'><div class='book_image'><img src='./uploadedImages/{serial5image}'></div><h1>{serial5name}</h1><p>By {serial5writer}</p><h4>{serial5price} Tk</h4><button class='buy_button'>See Details</button></div>" \
               f"</div><div id='footer' class='footer'><div class='footer_heading'><h1>CONNECT WITH US</h1></div>" \
               f"<div class='contact_input' id='contact_input'><div class='contact_input_center'><form method='post' action='contact.py'><div class='part'><label for='user_name'>Name</label><br><input name='userName' type='text' id='user_name' placeholder='Enter your name' required></div><br>" \
               f"<div class='part'><label for='user_email'>Email</label><br><input name='userEmail' type='text' id='user_email' placeholder='Enter your email' required></div><br>" \
               f"<div class='part'><label for='user_text'>Message</label><br><input name='userMessage' type='text' id='user_text' placeholder='Type your message' required></div><br>" \
               f"<button type='submit'>Send Message</button></form></div></div></div></body>" \
               f"</html>"

with open("home.html", "w") as html_file:
    html_file.write(html_content)
