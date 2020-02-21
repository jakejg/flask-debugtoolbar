from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolBarExtension
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "secret"
debug = DebugToolBarExtension(app)


@app.route('/')
def home():
    html = """
    <h1>Home Page</h1>
    <a href='/hello'> Go to Hello Page </a> <br>
    <a href='/search'> Go to Search Page </a>
    """
    return render_template("index.html")

@app.route('/hello')
def say_hello():
    return "Hello There!"

@app.route('/search')
def search():
    term = request.args['term']
    html = f"<h1> Search term: {term}"
    return html
    
@app.route('/post', methods=['post'])
def post():
    return "Post request made"