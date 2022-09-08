import sqlite3

connection = sqlite3.connect('my_capstone.db')
c = connection.cursor()

def view_all():
    view = "SELECT * FROM Users;"
    rows = c.execute(view).fetchall()

    for row in rows:
        user_id = row[0] if row[0] != None else "" 
        first_name = row[1] if row [1] != None else ""
        last_name = row[2] if row [2] != None else ""
        phone = row[3] if row[3] != None else ""
        email = row[4] if row[4] != None else ""
        password = row[5] if row[5] != None else ""
        active = row[6] if row[6] != None else ""
        date_created = row[7] if row[7] != None else ""
        hire_date = row[8] if row[8]!= None else ""
        user_type = row[9] if row[9]!= None else ""

        print(f'\n {user_id}. \n {first_name} {last_name} \n {phone} \n {email}\n {date_created} {hire_date} {user_type}\n')
    input('Press Enter to continue:')


def search_name(new_name, last_nam):
    new_name = '%' + new_name + '%'
    last_nam = '%' + last_nam +'%'
    search = "SELECT * FROM Users WHERE first_name Like ? OR last_name Like ?;"
    rows = c.execute(search,(new_name,last_nam)).fetchall()
    
    for row in rows:
        user_id = row[0] if row[0] != None else ""
        first_name = row[1] if row[1] != None else ""
        last_name = row[2] if row[2] != None else ""
        phone = row[3] if row[3] != None else ""
        email = row[4] if row[4] != None else ""
        hire_date = row[5] if row[5] != None else ""
        user_type = row[6] if row[6] != None else ""
        
        print(f'{user_id} {first_name} {last_name} {phone}  {email}  {hire_date} {user_type}')

#view_all()
# name = input('Please Enter a name you would like to find: ')
# last_nam= input('Pleae Enter a last name you would to find: ')    
# search_name(name, last_nam)

def view_active():
    view = "SELECT * FROM Users Where user_type is 'user' ORDER BY active = 1 ;"
    rows = c.execute(view).fetchall()

    for row in rows:
        user_id = row[0] if row[0] != None else "" 
        first_name = row[1] if row [1] != None else ""
        last_name = row[2] if row [2] != None else ""
        phone = row[3] if row[3] != None else ""
        email = row[4] if row[4] != None else ""
        password = row[5] if row[5] != None else ""
        active = row[6] if row[6] != None else ""
        date_created = row[7] if row[7] != None else ""
        hire_date = row[8] if row[8]!= None else ""
        user_type = row[9] if row[9]!= None else ""

        print(f'\n {user_id}. \n {first_name} {last_name} \n {phone} \n {email}\n {date_created} {hire_date} {user_type}\n')
    # input('Press Enter to continue:')
def view_user(new_name):
        
    new_name = '%' + new_name + '%'
    search = "SELECT * FROM Users WHERE first_name Like ?;"
    rows = c.execute(search,(new_name,)).fetchone()
    return rows


