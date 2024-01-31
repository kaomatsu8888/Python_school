import pandas as pd
import openpyxl

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# ソート(国語の点数が高い順に)
kokugo = df.sort_values("国語", ascending=False) # ascending=Falseで降順に

# エクセルファイルに書き出す
kokugo.to_excel("csv_to_excel.xlsx", sheet_name="国語") # シート名を指定して書き出し
