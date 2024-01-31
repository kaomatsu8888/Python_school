# CSVファイルに出力する
import os
import pandas as pd

current_directory = os.getcwd()# デバッグ用
print("現在のディレクトリ:", current_directory)# デバッグ用


# CSVファイルを読み込む
df = pd.read_csv("test.csv")
print("CSVファイルを読み込みました。") # デバッグ用

# ソート（国語の点数が高いもの順）
kokugo = df.sort_values(by="国語", ascending=False)
print("国語の点数が高いもの順でソート\n", kokugo) # デバッグ用

# CSVファイルに出力する
kokugo.to_csv("export1.csv")
print("CSVファイルに出力しました。") # デバッグ用

