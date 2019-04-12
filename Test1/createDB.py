import sqlite3
import os

cwd = os.getcwd()
create_table_contact_info = """ CREATE TABLE contacts (
                                UID INTEGER PRIMARY KEY,
                                Name TEXT NOT NULL,
                                Contact_Number TEXT NOT NULL,
                                Address TEXT NOT NULL,
                                Gender TEXT NOT NULL,
                                Sport TEXT NOT NULL,
                                Member_Status TEXT NOT NULL,
                                Comments TEXT NOT NULL
                                ); """

def connect_db(db_name):
    db_file = r"%s\%s" % (cwd, db_name)
    return sqlite3.connect(db_file)

    
def execute_query(sql_query):
    con = connect_db('sports_academy.db')  
    con.execute(sql_query)

def main():
    execute_query(create_table_contact_info)
    


main()