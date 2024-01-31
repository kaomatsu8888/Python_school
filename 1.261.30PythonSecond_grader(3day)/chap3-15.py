import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む(名前の列をインデックスで)
df = pd.read_csv("test.csv", index_col=0) # index_col=0はインデックスを0列目にするという意味

# 棒グラフを作って表示する
df.plot.bar() # barは棒グラフ
plt.legend(loc="lower right")
plt.show() # showは表示する

# 棒グラフ（水平）を作って表示する
df.plot.barh() # barhは水平棒グラフ
plt.legend(loc="lower right")
plt.show() # showは表示する

# 積み上げ棒グラフを作って表示する
df.plot.bar(stacked=True) # stacked=Trueは積み上げ棒グラフ. stackedは積み上げるという意味.
plt.legend(loc="lower right") # loc="lower right"は凡例を右下に表示するという意味
plt.show()

# 箱ひげグラフを作って表示する
df.plot.box() # boxは箱ひげグラフ
plt.show()

# 面グラフを作って表示する
df.plot.area()  # areaは面グラフ
plt.legend(loc="lower right") # loc="lower right"は凡例を右下に表示するという意味
plt.show()
