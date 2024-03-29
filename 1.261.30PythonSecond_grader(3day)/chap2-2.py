import requests # webページを取得するためのライブラリ
from bs4 import BeautifulSoup # HTMLやXMLファイルを解析するためのライブラリ。

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url) # 指定されたURLのWebページを取得します。
soup = BeautifulSoup(html.content, "html.parser") # BeautifulSoupの初期化/解析を行い, soupに格納します。

# title,h2,liタグを検索して表示する
print(soup.find("title")) # titleタグを検索して表示します。
print(soup.find("h2")) # h2タグを検索して表示します。
print(soup.find("li")) # liタグを検索して表示します。

