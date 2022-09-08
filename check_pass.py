
import bcrypt
import sqlite3
from admin import *
from user import *
connection = sqlite3.connect('my_capstone.db')
c = connection.cursor()


user_name = ''


def login():
    global user_name
    user_name = input("\nPlease enter your username: ")
    password = input("\nPlease enter your password: ")

    c.execute("SELECT user_id FROM Users WHERE email=? AND password=? AND active = 1", (user_name, password)).fetchone()

    password_encoded = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_encoded, salt)

# print(login())


def is_manager():
    global user_name
    user_type = ''

    # login()
   
    user = c.execute("SELECT user_type FROM Users WHERE email=?",(user_name,)).fetchone()
    
    if user and user[0] == 'Admin':
        user_type = '1'
        admin_menu()
    if user and user[0] == 'User':
        user_type = '0'
        user_menu()

    # return user_type


print(is_manager())
# print(user_type)