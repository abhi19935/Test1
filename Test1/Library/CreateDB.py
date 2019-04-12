import sqlite3
import os
cwd = os.getcwd()

def connect_db(db_name):
    db_file = r"%s\%s" % (cwd, db_name)
    return sqlite3.connect(db_file)

def execute_sql(conn, sql):
        c = conn.cursor()
        c.execute(sql)
        c.close()


def main():
    con = connect_db('test.db')
    drop_employer = 'DROP TABLE IF EXISTS Employer;'
    create_employer = '''CREATE TABLE Employer
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         NAME           VARCHAR    NOT NULL,
         ADDRESS        CHAR(50));'''
         
    drop_project = 'DROP TABLE IF EXISTS Project;'
    create_project = '''CREATE TABLE Project
         (Project_Name PRIMARY KEY     NOT NULL,
         Team_Members  INT,
         Country       VARCHAR,
         Company VARCHAR
         --ForeignKey(Company) REFERENCES Employer(ID)
         );'''
         
    insert_employer1 = '''INSERT INTO Employer(NAME,ADDRESS)
                        VALUES ('HCL','Sector-126,Noida' ); '''
    insert_employer2 = '''INSERT INTO Employer(NAME,ADDRESS)
                        VALUES ('TCS','Sector-135,Noida' ); '''
    insert_employer3 = '''INSERT INTO Employer(NAME,ADDRESS)
                        VALUES ('UHG','Sector-144,Noida' ); '''
    insert_project1 =  '''INSERT INTO Project(Project_Name,Team_Members,
                          Country,Company )
                        VALUES ('DWP',18, 'Germany','HCL'); '''
    insert_project2 =  '''INSERT INTO Project(Project_Name,Team_Members,
                          Country,Company )
                        VALUES ('ALDO',6, 'Canada', 'TCS'); '''
    insert_project3 =  '''INSERT INTO Project(Project_Name,Team_Members,
                          Country,Company )
                        VALUES ('B2B EDI',13, 'US', 'UHG'); '''
         
    if con is not None:
        execute_sql(con,drop_employer)
        execute_sql(con,drop_project)
        execute_sql(con,create_employer)
        execute_sql(con, create_project)
        execute_sql(con, insert_employer1)
        execute_sql(con, insert_employer2)
        execute_sql(con, insert_employer3)
        execute_sql(con, insert_project1)
        execute_sql(con, insert_project2)
        execute_sql(con, insert_project3) 
        print('data entry successful')
        con.commit()
        
    else:
        print("Database connection not active")
        
    con.close()
        

if __name__ == '__main__':
    main()
        