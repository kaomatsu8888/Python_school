# サイト構成変化のため使用不可
import requests
from bs4 import BeautifulSoup

# webページを取得して解析する
load_url = "https://www.yahoo.co.jp/categories/it"
html = requests.get(load_url) # 指定されたURLのWebページを取得します。
soup = BeautifulSoup(html.content, "html.parser") # BeautifulSoupの初期化/解析を行い, soupに格納します。

# classで検索し、その中のすべてのaタグを検索して表示する
topic = soup.find(class_="sc-apgtCX jcuqfq") # class_="topicsList_main"と同じです。
for element in topic.find_all("a"): # aタグを取得します。
    print(element.text) # .textをつけるとタグを除いた文字列を取得できます。
