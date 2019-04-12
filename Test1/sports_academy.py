#import sqlite3
import os
from flask_cors import CORS
from flask import render_template, request, redirect, session
from flask import Flask
import sqlite3
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
CORS(app)
app.debug = True
cwd = os.getcwd()

page_owner = 'Abhishek Chaubey'

#class ReusableForm(Form):
#    name = TextField('Name:', validators=[validators.required()])
#    password = TextField('Password:', validators=[validators.required()])

def getcurrtime():
    import time
    t1 = (time.strftime("%d%m%Y%H%M%S"))
    return t1

def connect_db(db_name):
    db_file = r"%s\%s" % (cwd, db_name)
    return sqlite3.connect(db_file)

    
def execute_query(sql_query):
    con = connect_db('sports_academy.db')  
    cur = con.cursor()
    if con:
        print('db connected')
    else:
        print('db not connected')
#    sql_query = """ INSERT INTO contacts Values
#                                (10001,
#                                'abhishek',
#                                '7701822',
#                                'sdfsdfsd',
#                                'male',
#                                'sdfsdsd',
#                                'active',
#                                'asdasasdasa'); """
#                                
    cur.execute(sql_query)
    con.commit()
    con.close()
    
# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
#    form = ReusableForm(request.form)
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('/home')
    return render_template('mylogin.html', error=error)
    
@app.route('/home')
def home():
    if session.get('logged_in'):
        print('logged in')
    return render_template('home.html')

@app.route('/entryform',  methods = ['GET','POST'])
#@app.route('/index', methods = ['GET','POST'])
def index():
    return render_template('sports_academy_input.html', page_owner=page_owner)

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':          
            name = request.form['name']
            contact = request.form['contact']
            address = request.form['address']
            gender = request.form['gender']
            sport = request.form['sports']
            member = request.form['status']
            comment = request.form['message']
            uid = getcurrtime()
        
            print(name)
            print(contact)
            print(address)
            print(gender)
            print(sport)
            print(member)
            print(comment)
        
            insert_query = """ INSERT INTO contacts VALUES 
                                ('"""+uid+"""',
                                '"""+name+"""',
                                '"""+contact+"""',
                                '"""+address+"""',
                                '"""+gender+"""',
                                '"""+sport+"""',
                                '"""+member+"""',
                                '"""+comment+"""'); """
            print(insert_query)
            
            execute_query(insert_query)
        
    return render_template("result.html",msg = 'data inserted successfully')


@app.route('/list')
def list():
   con = connect_db('sports_academy.db')
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from contacts")
   
   rows = cur.fetchall(); 
   print(rows)
   return render_template("list.html",rows = rows)



#   if request.method == 'POST':
#      try:
#         nm = request.form['nm']
#         addr = request.form['add']
#         city = request.form['city']
#         pin = request.form['pin']
#         
#         with sql.connect("database.db") as con:
#            cur = con.cursor()
#            cur.execute("INSERT INTO students (name,addr,city,pin) 
#               VALUES (?,?,?,?)",(nm,addr,city,pin) )
#            
#            con.commit()
#            msg = "Record successfully added"
#      except:
#         con.rollback()
#         msg = "error in insert operation"
#      
#      finally:
#         return render_template("result.html",msg = msg)
#         con.close()