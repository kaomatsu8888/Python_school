import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む(名前の列をインデックスで)
df = pd.read_csv("test.csv", index_col=0) # index_col=0はインデックスを0列目にするという意味

# 棒グラフを作って画像ファイルを出力する
colorlist = ["red", "blue", "green", "yellow", "purple", "orange"]
df.T.plot.bar(color=colorlist) # barは棒グラフ
plt.legend(loc="lower right")
plt.savefig("bargraph.png")
