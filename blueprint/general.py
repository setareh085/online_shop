from flask import Blueprint

app = Blueprint("general", __name__)
@app.route('/')
def main():  # put application's code here
    return 'Hello World!'

@app.route('/about')
def about():  # put application's code here
    return 'about page'