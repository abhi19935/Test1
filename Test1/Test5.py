from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.debug = True

org_details = {
        'hcl':{
        'Name': 'HCL',
        'Location': 'Noida-126',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/f/fa/ATR_ATR-42-300_F-WWEW_ATR%2C_Farnborough_UK%2C_September_1988._%285589254663%29.jpg'},
        'tcs':{
        'Name': 'TCS',
        'Location': 'Noida-135',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/8/82/Tata_Consultancy_Services_Vadapalani_2.JPG'},
        'uhg':{
        'Name': 'UHG',
        'Location': 'Noida-144',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/6/6b/Optum.jpg'}
        }

org_list = org_details.keys()
@app.route('/')
@app.route('/index')
def index():
    return render_template('myhomepage.html')

@app.route('/index/<org_initials>')
def org_name(org_initials):
    return render_template('org.html',
                           org_name = org_details[org_initials] )

@app.route('/contactus')
def contactus():
    return 'This is contactus page'

####################################################################
@app.route('/requestinfo')
@app.route('/index/requestinfo')
def request_info():
    # Get location info using https://freegeoip.net/
    geoip_url = 'http://freegeoip.net/json/{}'.format(request.remote_addr)
    client_location = requests.get(geoip_url).json()
    return render_template('info.html',
                           client_location=client_location)
####################################################################