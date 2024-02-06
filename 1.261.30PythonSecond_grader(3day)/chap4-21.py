import pandas as pd

# データフレームを読み込む
df = pd.read_csv("898.csv")

#　店舗のある拠点（緯度、経度）と店舗名をリスト化する
store = df[["緯度", "経度", "店舗名(日本語)"]].values # 店舗のある拠点（緯度、経度）と店舗名をリスト化する
print(len(store))  # データの個数を表示
print(store)
