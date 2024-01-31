import pandas as pd

# CSVファイルを読み込む（データフレーム形式）
df = pd.read_csv("test.csv")

# 「名前」の列を削除
print("「名前」の列を削除\n",df.drop("名前", axis=1)) # axisは軸の方向を指定する。axis=1は列方向、axis=0は行方向

# インデックス2行を削除
print("インデックス2行を削除\n",df.drop(2, axis=0))
