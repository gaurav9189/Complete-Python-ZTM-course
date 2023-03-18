from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/')
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.find_all('div'))
# CSS is used to select and style elemts of html for example a class is addressed as .class
# other elements such as links can be accessed via select('a') because 'a' represents an element in html referring to links
# Selectors you can use https://www.w3schools.com/cssref/css_selectors.php
links = soup.select('.titleline')[0]
# print(links)
scores = soup.select('.score')[0]
print(links.select('a')[0].get('href'))
# To get the text relevant to a class of score
print(scores.get_text())
# for score in scores:
#     print(score.text.split(' ')[0])
