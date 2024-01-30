import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url) # webページを取得する

response.encoding = response.apparent_encoding # 文字コードを変換する

filename = "download.txt"
f = open(filename, "w", encoding="utf-8")

f.write(response.text) # 取得したwebページを表示する

f.close()
