from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return "<strong>" + function() + "</strong>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>" 
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1 style = "text-align:center;">Hello, World!</h1>' \
            '<p>This is a paragraph</p>' \
            '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-YiLiX4vd2xYSEhWx9OLIvbLx2NNRMYd_Shd2pPz76mjWvbEBhQchem1nZEUp4CHakBU&usqp=CAU">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return 'bye'

# We can either use the commands
# set FLASK_APP=hello1.py
# $env:FLASK_APP='Flask/hello1.py'
# flask run

#or use this
@app.route('/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, you are {number} years old"

if __name__ == '__main__':
    app.run(debug=True)