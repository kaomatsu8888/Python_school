import requests
from bs4 import BeautifulSoup
import urllib

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのaタグを検索して、リンクを表示する
for element in soup.find_all("a"):# aタグを取得します。
    print(element.text) # .textをつけるとタグを除いた文字列を取得できます。
    url = (element.get("href")) # .get("href")でhref属性の値を取得できます。
    link_url = urllib.parse.urljoin(load_url, url) # 絶対URLに変換します。
    print(link_url) # 絶対URLを表示します。

