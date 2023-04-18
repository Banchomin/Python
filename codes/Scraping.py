# 허준 페이지 이름 웹 스크래핑
import requests
from bs4 import BeautifulSoup as bs

page = requests.get('https://hy24.kr/')
soup = bs(page.text, "html.parser")

element = soup.select('html > body > div#main > h1')

# print(element.text)
# print(page)
# print(soup)
print(element[0].text)
