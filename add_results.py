import sqlite3

connection = sqlite3.connect('my_capstone.db')
c = connection.cursor()

def create_results(user_id, assessment_id, score, assessment_date, admin_id):
       

    insert_sql ='''INSERT INTO AssessmentResults(user_id, assessment_id, score, assessment_date, admin_id)
    values(?,?,?,?,?);'''
    values = (user_id, assessment_id, score, assessment_date, admin_id,)
    c.execute(insert_sql,values)
    connection.commit()
    print(f'SUCCESS:  RESULTS was Successfully added!')



def add():    
    user_id = input("Please Enter user ID: ")
    assessment_id = input("Please Enter assessment Number: ")
    score  = input("Please Enter score received 0-4: ")
    assessment_date = input("Please Enter the date of the assessment was taken yyyy-mm-dd:")
    admin_id = input("Please Enter Admin_id:")

    create_results(user_id, assessment_id, score, assessment_date, admin_id)

add()