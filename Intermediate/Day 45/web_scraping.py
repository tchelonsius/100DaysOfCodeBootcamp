from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup)
titles = [item.text for item in soup.find_all(name="span", class_="titleline")]
links = [item.find(name="a").get("href") for item in soup.find_all(name="span", class_="titleline")]
points = [item.text for item in soup.find_all(name="span", class_="score")]

greatest = 0
index = 0
for f in range(len(points)):
    value = int(points[f].split(" ")[0])
    if value > greatest:
        index = f
        greatest = value
print(titles[index])
print(links[index])
print(greatest)