import requests
import json
from pprint import pprint

# 現在の天気を取得する：神戸
url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Kobe,JP", key="c649a76bc4431b260edb4b21a56a3068")

jsondata = requests.get(url).json()
pprint(jsondata)
