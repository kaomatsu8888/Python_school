import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('test.csv') # ファイル名を指定する.dfはDataFrameの略

#　表データの情報を表示する
print("データの件数 =",len(df))
print("項目名      =", df.columns.values)
print("インデックス=", df.index.values)
