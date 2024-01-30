import requests

url = "https://www.ymori.com/books/python2nen/test1.html" # webページのURLを指定する
response = requests.get(url) # webページを取得する

response.encoding = response.apparent_encoding # 文字コードを変換する

filename = "download.txt" # 保存するファイル名を指定する
f = open(filename, "w", encoding="utf-8") # ファイルを開く

f.write(response.text) # 取得したwebページを表示する

f.close() # ファイルを閉じる
