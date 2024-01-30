import requests
from bs4 import BeautifulSoup

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのaタグを検索して、リンクを表示する
for element in soup.find_all("a"):# aタグを取得します。
    print(element.text) # .textをつけるとタグを除いた文字列を取得できます。
    print(element.get("href")) # .get("href")でhref属性の値を取得できます。
