from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    org_name = "HCL"
    return render_template('index2.html', org_name = org_name)

@app.route('/contactus')
def contactus():
    return 'This is contactus page'
    