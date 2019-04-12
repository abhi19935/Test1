from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    #html = "afjaskjajjaklajkl"
    html = """
        <html>
            <h1>Welcome to our HomePage</h1>
            <ul>
                <li>HCL</li>
                <li>TCS</li>
                <li>UHG</li>
            </ul>   
        </html>
    """
    return html