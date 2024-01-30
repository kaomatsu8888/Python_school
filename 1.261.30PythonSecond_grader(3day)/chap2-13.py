import requests
from bs4 import BeautifulSoup
import urllib

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのimgタグを検索して、リンクを表示する
for element in soup.find_all("img"):# すべてのimgタグを取得します。
    src = (element.get("src")) # .get("src")でsrc属性の値を取得できます。

    # 絶対URLと、ファイルを表示する
    image_url = urllib.parse.urljoin(load_url, src) # 絶対URLに変換します。
    finename = image_url.split("/")[-1] # 画像ファイル名を取得します。
    print(image_url) # 絶対URLを表示します。

# imgタグを変えてみたら、どうなるか試してみよう。
