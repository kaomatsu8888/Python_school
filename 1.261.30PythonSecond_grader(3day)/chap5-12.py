import requests
import json
from pprint import pprint
from datetime import datetime, timedelta, timezone
import pandas as pd

# 5日間（3時間ごとの）の天気を取得する：東京
url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Tokyo,JP", key="c649a76bc4431b260edb4b21a56a3068")

jsondata = requests.get(url).json()
df = pd.DataFrame(columns=["気温"])
tz = timezone(timedelta(hours=+9), 'JST')
for dat in jsondata["list"]:
	jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
	temp = dat["main"]["temp"]
	df.loc[jst] = temp

pprint(df)
