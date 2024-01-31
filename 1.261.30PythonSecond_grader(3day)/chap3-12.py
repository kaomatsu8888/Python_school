#　インデックスを削除してCSVファイルに出力
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# ソート（国語の点数が高いもの順）
kokugo = df.sort_values(by="国語", ascending=False)

# CSVファイルに出力する(インデックスを削除)
kokugo.to_csv("export2.csv", index=False)
