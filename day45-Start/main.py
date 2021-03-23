from bs4 import BeautifulSoup
import requests

response = requests.get(url = "https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
link_list = []
final_list = []
first_story = soup.find_all(name = "a", class_ = "storylink")
for story in first_story:
    a = {}
    a["Story"] = story.getText()
    a["StoryLink"] = story.get("href")
    link_list.append(a)
first_upvote = soup.find_all(name = "span", class_ = "score")
max = -1
pos = -1
for i in range(0,len(first_upvote)):
    number = int(first_upvote[i].getText().split(" ")[0])
    if number > max:
        max = number
        pos = i



for i in range(0,len(first_upvote)):
    a = link_list[i]
    b = first_upvote[i]
    a["upvotes"] = b.getText()
    final_list.append(a)

# print(final_list) 
print(final_list[pos])

## To print out article with max upvotes




# fhand = open("./day45-Start/website.html")
# contents = fhand.read()
# # print(contents)
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# all_anchor = soup.find_all(name = "a")
# print(all_anchor)
# for tag in all_anchor:
#     print(tag.getText())

# for tag in all_anchor:
#     print(tag.get("href"))

# print(soup.find(name = "h1", id = "name"))
# print(soup.select(selector = "p a"))