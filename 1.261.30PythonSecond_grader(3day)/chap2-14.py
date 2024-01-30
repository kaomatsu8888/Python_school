import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url) # webページを取得する
soup = BeautifulSoup(html.content, "html.parser") # parserは解析の方法

# 保存用フォルダを作る
out_folder = Path("download2") # download2というフォルダを作る
out_folder.mkdir(exist_ok=True) # すでにフォルダがある場合は何もしない

# すべてのimgタグを検索して、リンクを表示する
for element in soup.find_all("img"): # すべてのimgタグを取得します。
    src = element.get("src") # .get("src")でsrc属性の値を取得できます。

    # 絶対URLと、ファイルを表示する
    image_url = urllib.parse.urljoin(load_url, src) # 絶対URLに変換します。
    imagedata = requests.get(image_url) # 画像データを取得する

    # URLから最後のファイル名を取り出して、ファイル名を作る
    filename = image_url.split("/")[-1] # 画像ファイル名を取得します。
    out_path = out_folder.joinpath(filename) # 保存ファイル名を作る

    # ファイルを保存する
    with open(out_path, mode="wb") as f:
        f.write(imagedata.content) # 画像データを書き込む
    
    # 1秒間のインターバルを入れる
    time.sleep(1)
