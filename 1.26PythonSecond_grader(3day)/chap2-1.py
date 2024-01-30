import requests
from bs4 import BeautifulSoup

# wewbページを取得する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# html全体を表示する
print(soup)
