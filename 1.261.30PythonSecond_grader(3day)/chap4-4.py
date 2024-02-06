import pandas as pd

# データフレームを読み込む
df = pd.read_csv("FEH_00200524_190618234018.csv",index_col="全国・都道府県", encoding="shift_jis")  # CSVファイル用の関数と正しい引数を使用
print(len(df)) # データフレームの行数を表示
print(df.columns.values)# データフレームの列名を表示
