from flask import Flask, render_template
from post import Post

app = Flask(__name__)

p = Post()
posts = p.all_posts


@app.route('/')
def home():
    return render_template("index.html", post = posts, length = len(posts))

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    post_a = posts[blog_id]
    return render_template("post.html", post = post_a)
    

if __name__ == "__main__":
    app.run(debug=True)
