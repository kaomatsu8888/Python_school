import requests

# 画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url) # 画像ファイルを取得する

# URLから最後のファイル名を取り出す
filename = image_url.split("/")[-1] # URLを/で分割し、最後の要素を取り出す

# ファイルをバイナリモードで保存する/文字列になっているからバイナリモードで保存する
with open(filename, mode="wb") as f:
    f.write(imgdata.content) # content属性から画像データを取得する
