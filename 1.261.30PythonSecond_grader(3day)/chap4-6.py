import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込む
df = pd.read_csv("FEH_00200524_190618234018.csv",index_col="全国・都道府県", encoding="shift_jis")  # CSVファイル用の関数と正しい引数を使用

# 平生30年の列データで棒グラフを作成して表示する
df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",",""))  # カンマを削除して数値に変換
print(df["平成30年"]) # 「平成30年」の列を表示
df["平成30年"].plot.bar()
plt.show()
