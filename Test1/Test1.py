from flask import Flask

app = Flask(__name__)
#app.debug = False


@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/contactus')
def contactus():
    return 'This is contactus page'

