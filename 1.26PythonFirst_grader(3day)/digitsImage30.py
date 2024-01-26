# digitsImage50.py
import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits() #データセットを読み込む

for i in range(50): #0から49まで繰り返す
    plt.subplot(5, 10, i+1) #5行10列のグラフのi+1番目に描画する
    plt.axis("off") #軸目盛を消す
    plt.title(digits.target[i]) #タイトルにラベルを表示する
    plt.imshow(digits.images[i], cmap="Greys") #画像を表示する
plt.show() #グラフを表示する
