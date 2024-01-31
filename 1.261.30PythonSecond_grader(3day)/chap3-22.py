import pandas as pd
import openpyxl

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# ソート(国語の点数が高い順に)
kokugo = df.sort_values("国語", ascending=False) # ascending=Falseで降順に

# １つのエクセルファイルに複数のシートで書き出す
with pd.ExcelWriter("csv_to_excel3.xlsx") as writer: # ExcelWriterを使うとwithブロック内でExcelファイルを扱える
    df.to_excel(writer, index=False, sheet_name="元のデータ") # シート名を指定して書き出し
    kokugo.to_excel(writer, sheet_name="国語でソート") # シート名を指定して書き出し

