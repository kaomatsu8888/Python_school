#学習用数値データを画像化する
import sklearn.datasets #データセットを読み込むために必要
import matplotlib.pyplot as plt #画像を表示するために必要

digits = sklearn.datasets.load_digits() #データセットを読み込む

plt.imshow(digits.images[0], cmap="Greys") #画像を表示する
plt.show() #画像を表示する
