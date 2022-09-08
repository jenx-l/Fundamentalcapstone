import sqlite3

connection = sqlite3.connect('my_capstone.db')
c = connection.cursor()

def create_assessment(assessment_type,assessment_description,due_date,creation_date,competency_id):
       

    insert_sql ='''INSERT INTO Assessments (assessment_type,assessment_description,due_date,creation_date,competency_id)
    values(?,?,?,?,?);'''
    values = (assessment_type,assessment_description,due_date,creation_date,competency_id,)
    c.execute(insert_sql,values)
    connection.commit()
    print(f'SUCCESS:  assessment was Successfully added!')



def add():    
    assessment_type = input("Please Enter assessment type: ")
    assessment_description = input("Please Enter assessment description: ")
    due_date  = input("Please Enter due date yyyy-mm-dd: ")
    creation_date = input("Please Enter today's date yyyy-mm-dd:")
    competency_id = input("competency_id:")

    create_assessment(assessment_type,assessment_description,due_date,creation_date,competency_id)

add()
