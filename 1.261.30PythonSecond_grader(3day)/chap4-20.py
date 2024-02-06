import pandas as pd

# データフレームを読み込む
df = pd.read_csv("898.csv")

print(len(df))  # データの個数を表示
print(df.columns.values)  # カラム名を表示
