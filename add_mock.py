import sqlite3
import my_class
import bcrypt

def add_values():
    connection = sqlite3.connect('my_capstone.db')
    db_cursor = connection.cursor()

    with open('mock_data.csv') as my_csv:
        for row in my_csv:
            values = row.strip().split(',')
            # print(values)

            class_user = my_class.User(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8])

            users ="""INSERT INTO Users (first_name,last_name,phone,email,password,active,date_created,hire_date,
        user_type) values(?,?,?,?,?,?,?,?,?);"""    

            first_name = class_user.first_name
            last_name = class_user.last_name
            phone = class_user.phone
            email = class_user.email
            password = (class_user.password).decode()
            active= class_user.active
            date_created = class_user.date_created
            hire_date = class_user.hire_date
            user_type = class_user.user_type

            db_cursor.execute(users,(first_name,last_name,phone,email,password,active,date_created,hire_date,user_type))
    connection.commit()
add_values()

