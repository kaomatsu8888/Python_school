import tkinter as tk #ウィンドウを表示するモジュール
import tkinter.filedialog as fd #ファイルダイアログを扱うモジュール
import PIL.Image #画像を扱うモジュール
import PIL.ImageTk #tkinterで作った画面上に画像を表示されるモジュール

def dispPhoto(path): #画像ファイルを表示する関数
    #画像を読み込む
    newImage = PIL.Image.open(path).convert("L").resize((32,32)).resize((300,300), resample=0)#パス指定.グレースケール変換.サイズ変更.モザイク処理
    #そのイメージをラベルに表示する
    imageDate = PIL.ImageTk.PhotoImage(newImage)#ここから3行はイメージをラベルに表示する
    imageLabel.configure(image = imageDate )
    imageLabel.image = imageDate

def openFile(): #ファイルのダイアログを開くための関数
    fpath = fd.askopenfilename()#ファイルダイアログを開いて、選択したファイル名を取得
    if fpath: #もしファイル名があったら
        dispPhoto(fpath)#そのファイル名で関数を呼び出す

root = tk.Tk() #画面を作る
root.geometry("400x350") #画面をつくる

btn = tk.Button(text="ファイルを開く", command = openFile) #ボタンを作って関数を設定する
imageLabel = tk.Label() #画面表示用のラベルを作る
btn.pack() #画面にボタンを配置する
imageLabel.pack() #画面にラベルを配置する
tk.mainloop() #作ったウィンドウを表示する
