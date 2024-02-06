import pandas as pd

# データフレームを読み込む
df = pd.read_csv("13TOKYO.CSV", header=None, encoding="shift_jis")  # CSVファイル用の関数と正しい引数を使用
print(len(df)) # データフレームの行数を表示
print(df.columns.values)　# データフレームの列名を表示
