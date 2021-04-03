import requests
class Post:
    def __init__(self):
        blog_url = "https://api.npoint.io/4c5a7d952f3cfc125dce"
        response = requests.get(url= blog_url)
        self.all_posts = response.json()