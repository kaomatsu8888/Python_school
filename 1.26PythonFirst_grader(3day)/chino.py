
import tkinter as tk 
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
# 機械学習で使うモジュールを読み込む
import sklearn.datasets
import sklearn.svm
import numpy

# 画像ファイルを数値リストに変換する
def imageToData(filename):
    # 画像を8x8のグレースケールに変換し、数字の配列に変換する
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8), PIL.Image.Resampling.LANCZOS)
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300, 300),resample=0))
    imageLabel.configure(image=dispImage) # 画像を表示する
    imageLabel.image = dispImage # 画像を再表示するために、変数に代入しておく
    # 数値リストに変換
    numImage = numpy.asarray(grayImage, dtype=float) # float型に変換.dtypeはデータ型を表す
    numImage = 16 - numpy.floor(16 * (numImage / 256)) # 0-255の値を0-15に変換
    numImage = numImage.flatten() # 一次元の配列に変換
    return numImage 

# 数字を予測する
def predictDigits(data):
    # 学習用データを読み込む
    digits = sklearn.datasets.load_digits() # 0-9の手書き数字のデータセット
    # 機械学習する
    clf = sklearn.svm.SVC(gamma=0.001) # サポートベクターマシン
    clf.fit(digits.data, digits.target)
    # 予測結果を表示する
    n = clf.predict([data])
    textLabel.configure(text="この画像は"+str(n)+"です！")

# ファイルダイアログを開く
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        # 画像ファイルを数値リストに変換する
        data = imageToData(fpath)
        # 数字を予測する
        predictDigits(data)

# アプリのウィンドウを作る
root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root, text="ファイルを開く", command=openFile)
# 画像表示用のラベルを作る
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
# 予測結果のラベルを作る
textLabel = tk.Label(text="手書きの数字を認識します！")
textLabel.pack()

tk.mainloop()
