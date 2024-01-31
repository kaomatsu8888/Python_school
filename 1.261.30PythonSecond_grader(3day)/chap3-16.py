import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む
df = pd.read_csv("test.csv", index_col=0) # index_col=0はインデックスを0列目にするという意味

# 国語の棒グラフを作って表示する
df["国語"].plot.barh() # barhは水平棒グラフ
plt.legend(loc="lower left") # loc="lower right"は凡例を右下に表示するという意味.legendは凡例を表示する
plt.show() # showは表示する

# 国語と数学の棒グラフを作って表示する
df[["国語", "数学"]].plot.barh() # barhは水平棒グラフ
plt.legend(loc="lower left")
plt.show()

# C子の棒グラフを作って表示する
df.loc["C子"].plot.barh() # barhは水平棒グラフ
plt.legend(loc="lower left") # loc="lower right"は凡例を右下に表示するという意味
plt.show()

# C子の円グラフを作って表示する
df.loc["C子"].plot.pie(labeldistance=0.6) # pieは円グラフ. labeldistance=0.6はラベルを円の中心から0.6倍の距離にするという意味
plt.legend(loc="lower left")
plt.show()

