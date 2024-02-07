import json
from pprint import pprint

with open("test2.json", mode="r") as f: # ファイルを読み込む
    jsondata = json.loads(f.read()) # jsonファイルを読み込む
    print("1つ目のオブジェクト =", jsondata[0]) # 1つ目のオブジェクトを表示,jsondata[0]で1つ目のオブジェクトを取得
    print("都市名 =", jsondata[0]["name"]) # 都市名を表示
    print("緯度 =", jsondata[0]["coord"]["lat"]) # 緯度を表示
    print("経度 =", jsondata[0]["coord"]["lon"]) # 経度を表示
