from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

class MyForm(FlaskForm):
    email = StringField(label='email', validators= [DataRequired(), Email(message= 'Not a valid email')])
    password = PasswordField(label='password', validators= [DataRequired(), Length(min = 8, message="Atleast 8 characters required")])
    submit = SubmitField(label='submit')

app = Flask(__name__)
Bootstrap(app)

app.secret_key = "any-string-you-want-just-keep-it-secret"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    m = MyForm()
    if request.method == 'POST':
        if m.validate_on_submit():
            if m.email.data == 'aryan.shrivastava9@gmail.com' and m.password.data == '123456789':
                return render_template('success.html')
            elif m.email.data != 'aryan.shrivastava9@gmail.com' or m.password.data != '123456789':
                return render_template('denied.html')
    return render_template('login.html', form = m)



if __name__ == '__main__':
    app.run(debug=True)