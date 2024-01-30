import requests
from bs4 import BeautifulSoup

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url) # 指定されたURLのWebページを取得します。
soup = BeautifulSoup(html.content, "html.parser") # BeautifulSoupの初期化/解析を行い, soupに格納します。

# すべてのliタグを検索して表示する
for element in soup.find_all("li"):
    print(element.text) # .textをつけるとタグを除いた文字列を取得できます。
