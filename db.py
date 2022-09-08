import sqlite3

# def create_schema():
#     connection = sqlite3.connect('my_capstone.db')
#     db_cursor = connection.cursor()
#     with open('schema.sql', 'rt', encoding='utf-8') as schema:
#         queries = schema.read()
#         db_cursor.executescript(queries)
#     connection.commit()




def create_schema(cursor):
    with open('schema.sql','r') as infile:
        schema=infile.read()
        cursor.executescript(schema)
        connection.commit()
connection = sqlite3.connect('my_capstone.db')
cursor = connection.cursor()

# result = create_schema(cursor)
create_schema(cursor)