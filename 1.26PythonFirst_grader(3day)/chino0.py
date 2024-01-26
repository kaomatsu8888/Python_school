import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

# 画像ファイルを数値リストに変換する
def imageToData(filename):
    # 画像を8x8のグレースケールに変換し、数字の配列に変換する
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8), PIL.Image.Resampling.LANCZOS)

#　その画像を表示する
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300, 300),resample=0))
    imageLabel.configure(image=dispImage)
    imageLabel.image = dispImage

# ファイルダイアログを開く
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        # 画像ファイルを数値リストに変換する
        imageToData(fpath)

# アプリのウィンドウを作る
root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root, text="ファイルを開く", command=openFile)
# 画像表示用のラベルを作る
imageLabel = tk.Label()

btn.pack()
imageLabel.pack()

tk.mainloop()
