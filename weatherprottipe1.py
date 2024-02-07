import requests

# 現在の天気を取得する：東京
url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
jsondata = requests.get(url).json()

# 最初の timeSeries セクションから東京地方の情報を取得
tokyo_area_info = jsondata[0]['timeSeries'][0]['areas'][0]

# 都市名を取得
city_name = tokyo_area_info['area']['name']
print(f"都市名 = {city_name}")

# 天気予報を取得
weathers = tokyo_area_info['weathers'] # 3日間の天気予報
print("天気予報 =") # 天気予報を表示
for i, weather in enumerate(weathers, start=1): # 天気予報を表示
    print(f"  {i}日目: {weather}")
