import requests
from pathlib import Path

# 保存用フォルダを作る
out_folder = Path("download")
out_folder.mkdir(exist_ok=True) # すでにフォルダがある場合は何もしない(make directory)

# 画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url) # 画像ファイルを取得する

# URLから最後のファイル名を取り出し、保存フォルダ名と合体させる
filename = image_url.split("/")[-1] # URLを/で分割し、最後の要素を取り出す
out_path = out_folder.joinpath(filename) # ファイル名をつなげて保存パスを作る

# ファイルを保存する
with open(out_path, mode="wb") as f:
    f.write(imgdata.content) # content属性から画像データを取得する
