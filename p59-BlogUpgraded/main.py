from flask import Flask, render_template
import requests
app = Flask(__name__)

response = requests.get("https://api.npoint.io/0067e63917ca7a5034d9")
posts = response.json()

@app.route('/')
def index():
    return render_template("index.html", all_posts = posts, length = len(posts))

@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:blog_id>')
def post(blog_id):
    post = posts[blog_id]
    return render_template("post.html", post = post)

if __name__ == "__main__":
    app.run(debug=True)