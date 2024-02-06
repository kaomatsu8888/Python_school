import pandas as pd

# データフレームを読み込む
df = pd.read_csv("200.csv", encoding="shift_jis")  # CSVファイル用の関数と正しい引数を使用

# 消火栓のある地点の緯度経度を抽出して表示
hydrant = df[['緯度','経度']].values # 緯度と経度の列を抽出。リスト形式で抽出するためvaluesを使用
print(hydrant)
