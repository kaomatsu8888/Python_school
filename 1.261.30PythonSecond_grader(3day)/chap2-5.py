import requests
from bs4 import BeautifulSoup

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url) # 指定されたURLのWebページを取得します。
soup = BeautifulSoup(html.content, "html.parser") # BeautifulSoupの初期化/解析を行い, soupに格納します。

# IDで検索して表示する
chap2 = soup.find(id="chap2")
print(chap2)
