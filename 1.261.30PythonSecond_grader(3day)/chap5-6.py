import requests
import json
from pprint import pprint

# 現在の天気を取得する：神戸
url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Kobe,JP", key="c649a76bc4431b260edb4b21a56a3068")

jsondata = requests.get(url).json()
print("都市名 =", jsondata["name"]) # 都市名を表示
print("気温 =", jsondata["main"]["temp"]) # 気温を表示
print("天気 =", jsondata["weather"][0]["main"]) # 天気を表示
print("天気詳細 =", jsondata["weather"][0]["description"]) # 天気詳細を表示
print("最高気温 =", jsondata["main"]["temp_max"]) # 最高気温を表示
print("最低気温 =", jsondata["main"]["temp_min"]) # 最低気温を表示

