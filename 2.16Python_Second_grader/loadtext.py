import PySimpleGUI as sg
from pathlib import Path
import chardet 
sg.theme("DarkBrown3")

layout = [[sg.B(" ファイルを開く ", k="btn1"), sg.T(k="txt1")],
          [sg.ML(k="txt2", font=(None,14), size=(80,15))]]
win = sg.Window("テキストファイルの読み込み", layout)

def loadtext():
    global loadname, enc # 関数外の変数を関数内で使うための宣言
    loadname = sg.popup_get_file("テキストファイルを選択してください。")
    if not loadname: # キャンセルボタンが押された場合の処理/キャンセルボタンが押された場合、loadnameにはFalseが入る
        return
    with open(loadname, "rb") as f:
        b = f.read()
        enc = chardet.detect(b)["encoding"]
        p = Path(loadname)
        txt = p.read_text(encoding = enc)
        win["txt1"].update(loadname)
        win["txt2"].update(txt)
      
while True:
    e, v = win.read()
    if e == "btn1":
      loadtext()
    if e == None:
        break
win.close()
