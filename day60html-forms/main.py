from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        if request.form['fname'] == 'Aryan' and request.form['password'] == '123456A':
            username = request.form['fname']
            password = request.form['password']
            return f"<h1>Name : {username}</h1> <br> <h1>Password: {password}</h1>"
        else: 
            error = "Invalid Username or Password"
            return f"<h1>{error}</h1>"

if __name__ == '__main__':
    app.run(debug=True)