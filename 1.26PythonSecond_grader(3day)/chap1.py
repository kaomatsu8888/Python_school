import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url) # webページを取得する

response.encoding = response.apparent_encoding # 文字コードを変換する

print(response.text) # 取得したwebページを表示する
