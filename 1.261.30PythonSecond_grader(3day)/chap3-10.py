# 行と列を入れ替える
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 行と列を入れ替える
print("行と列を入れ替える\n", df.T)

# データをリスト化する
print("データをリスト化する\n", df.values)
