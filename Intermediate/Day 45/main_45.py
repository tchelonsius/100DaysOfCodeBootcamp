# Day 45: Using Beautiful Soup lib to parse html elements.
# This program parses the 100 best movies' names according
# to empireonline.com and creates a txt file containing these movies.

from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text


soup = BeautifulSoup(contents, "html.parser")
elements = soup.find_all(name="h3")
titles = []
years = []
final = ['' for f in range(100)]

aux = 0
for item in soup.find_all(name="p", class_="description"):
    year = item.text[0:4]
    if not year.isnumeric():
        year = ''
    years.append((aux, year))
    aux+=1

years.sort(key=lambda x: x[1], reverse = True)

with open("result.txt", "w") as file:
    file.write("")


for i in range(len(elements)):
    value = elements[i].text.encode("utf-8")
    value = str(value).split(") ")[-1][0:-1]
    titles.append(value)

for f in range(len(years)):
    final[f] = f"{f+1}) {titles[years[f][0]]} - {years[f][1]}"



with open("result.txt", "a") as file:
    for item in final:
        file.write(item+"\n")