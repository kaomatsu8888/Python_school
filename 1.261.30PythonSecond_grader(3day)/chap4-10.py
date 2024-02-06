import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込む
df = pd.read_csv("FEH_00200524_190618234018.csv",index_col="全国・都道府県", encoding="shift_jis")  # CSVファイル用の関数と正しい引数を使用

# 平生30年の列データで棒グラフを作成して表示する
df = df.drop("全国", axis=0)  # 全国の行を削除/axis=0は行を指定/axis=1は列を指定/
df["平成29年"] = pd.to_numeric(df["平成29年"].str.replace(",",""))  # カンマを削除して数値に変換
df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",",""))  # カンマを削除して数値に変換
df["人口増減"] = df["平成30年"] - df["平成29年"]  # 人口増減を計算
df = df.sort_values("人口増減", ascending=False)  # 並び替え
df["人口増減"].plot.bar(figsize=(10, 6)) # グラフのサイズを指定
plt.ylim(-40,140) # y軸の範囲を指定
plt.show()
