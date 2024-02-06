import pandas as pd
import folium

# データフレームを読み込む
df = pd.read_csv("200.csv", encoding="shift_jis")  # CSVファイル用の関数と正しい引数を使用

# 消火栓のある地点（緯度、経度）をリスト化する
hydrant = df[['緯度','経度']].values # 緯度と経度の列を抽出。リスト形式で抽出するためvaluesを使用

# 地図を作成
m = folium.Map(location=[35.942957, 136.198863], zoom_start=15) # 地図の中心を指定して作成
for data in hydrant:
    folium.Marker([data[0], data[1]]).add_to(m) # マーカーを作成
m.save("hydrant.html") # 地図を保存
