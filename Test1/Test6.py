import sqlite3
import os
from flask import render_template
from flask import Flask

app = Flask(__name__)
app.debug = True
cwd = os.getcwd()

def connect_db(db_name):
    db_file = r"%s\%s" % (cwd, db_name)
    return sqlite3.connect(db_file)

def get_data():
    con = connect_db('test.db')  
    sql_employer = 'select * from employer'    
    sql_project = 'select * from project'
    cursor_initials = con.execute(sql_employer)
    cursor_info = con.execute(sql_employer)
    cursor_project = con.execute(sql_project)
    project_info = cursor_project.fetchall()
    #results = cursor.fetchall()
    org_initials = [row[1].lower() for row in cursor_initials.fetchall()]
    org_info = [dict(name=rows[1], address=rows[2]) for rows in cursor_info.fetchall()]
    org_details = dict(zip(org_initials,org_info))
    

    for key in org_details.keys():
        for elements in project_info:
            temp_dict={}
            if key == elements[3].lower():
                temp_dict['project'] = elements[0]
                temp_dict['country'] = elements[2]                   
                org_details[key].update(temp_dict)
                
    cursor_initials.close()
    cursor_info.close()
    cursor_project.close()
    con.close()
    return org_details

org_details = get_data()

@app.route('/')
@app.route('/index')
def index():
    return render_template('myhomepage.html')


@app.route('/index/<org_initials>')
def org_name(org_initials):
    return render_template('org_db.html',
                           org_name = org_details[org_initials] )

@app.route('/contactus')
def contactus():
    return 'This is contactus page'