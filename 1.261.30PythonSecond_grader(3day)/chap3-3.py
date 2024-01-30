import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('test.csv') # ファイル名を指定する.dfはDataFrameの略

# 1列のデータを表示
print("国語の列データ\n", df["国語"]) # 1列のデータを表示する

# 複数列のデータを表示
print("国語と数学の列データ\n", df[["国語", "数学"]]) # 複数列のデータを表示する
