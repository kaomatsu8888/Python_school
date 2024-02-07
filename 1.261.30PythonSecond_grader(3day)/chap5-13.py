import requests
import json
from pprint import pprint
from datetime import datetime, timedelta, timezone
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# 5日間（3時間ごとの）の天気を取得する：東京
url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Tokyo,JP", key="c649a76bc4431b260edb4b21a56a3068")

jsondata = requests.get(url).json() # JSONデータを取得
df = pd.DataFrame(columns=["気温"]) # データフレームを作成.columnsで列名を指定
tz = timezone(timedelta(hours=+9), 'JST') # タイムゾーンを指定
for dat in jsondata["list"]: # データを取得
	jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9] # 日時を取得
	temp = dat["main"]["temp"] # 気温を取得
	df.loc[jst] = temp # データフレームに追加

df.plot(figsize=(15, 8)) # グラフを描画figsizeでグラフのサイズを指定
plt.ylim(-10, 40) # y軸の範囲を指定
plt.grid() # グリッドを表示
plt.show() # グラフを表示
