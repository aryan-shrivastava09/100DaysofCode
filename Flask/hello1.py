from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye():
    return 'bye'

# We can either use the commands
# set FLASK_APP=hello1.py
# $env:FLASK_APP='Flask/hello1.py'
# flask run

#or use this

if __name__ == '__main__':
    app.run()