
import bcrypt
import sqlite3
from admin import admin_menu
from user import user_menu

connection = sqlite3.connect('my_capstone.db')
c = connection.cursor()



def login():
    user_name = input("\nPlease enter your username: ")
    password = input("\nPlease enter your password: ")

    result = c.execute("SELECT user_id, password FROM Users WHERE email=? AND active = 1", (user_name,)).fetchone()
    if not result:
        print('Invalid username')
    hashed_pw = result[1].encode()
    password_encoded = password.encode("utf-8")
    
    check_password = bcrypt.checkpw(password_encoded, hashed_pw)
   # hashed = bcrypt.hashpw(password_encoded, salt)
    if check_password:
        print('CheckPass result ----', end="")
        print(check_password)
        is_manager(user_name)
# print(login())


def is_manager(user_name):
   
    user = c.execute("SELECT user_type FROM Users WHERE email=?",(user_name,)).fetchone()
    print(user)
    print('Hello from is_manager()')
    if user[0].lower() == 'admin':
       # user_type = '1'
        admin_menu()
    if user[0].lower() == 'user':
       # user_type = '0'
        user_menu()

    # return user_type


# print(is_manager())
# print(user_type)