from flask import Flask, render_template
import random
import requests
from datetime import datetime

d = datetime.now()

app = Flask(__name__)

@app.route('/')
def greet():
    random_number = random.randint(1,10)
    year = d.year
    name = "Aryan Srivastava"
    return render_template("index.html", num = random_number, current_year = year, my_name = name)

@app.route('/guess/<name>')
def guess(name):
    params= {
        "name" : name
    }
    response = requests.get(url= "https://api.agify.io", params= params)
    response.raise_for_status()
    data = response.json()
    name_person = data['name'].title()
    age_person = data['age']
    response2 = requests.get(url= "https://api.genderize.io", params= params)
    data2 = response2.json()
    gender_person = data2['gender']
    return render_template("guess.html", name = name_person, age = age_person, gender = gender_person)

@app.route('/blog/<int:num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/4c5a7d952f3cfc125dce"
    response = requests.get(url= blog_url)
    all_posts = response.json()
    number = num 
    return render_template('blog.html', posts = all_posts, post_no = number)

if __name__ == '__main__':
    app.run(debug=True)