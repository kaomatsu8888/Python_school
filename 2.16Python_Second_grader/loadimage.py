import PySimpleGUI as sg
from PIL import Image
import io
sg.theme("DarkBrown3")

layout = [[sg.B(" ファイルを開く ", k="btn1"), sg.T(k="txt")],
          [sg.Im(k="img")]]
win = sg.Window("画像ファイルを表示", layout, size=(320,380))

def loadimage(): # 画像ファイルを読み込む関数
    loadname = sg.popup_get_file("画像ファイルを選択してください。") # ファイル選択ダイアログを表示する。
    if not loadname: # キャンセルボタンが押された場合の処理/キャンセルボタンが押された場合、loadnameにはFalseが入る
        return
    try:
        img = Image.open(loadname)
        img.thumbnail((300,300))
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        win["img"].update(data=bio.getvalue())
        win["txt"].update(loadname)
    except:
        win["img"].update()
        win["txt"].update("失敗しました。")

while True: # イベントループ
    e, v = win.read() # イベントを待つ
    if e == "btn1": # ボタンが押された場合の処理
      loadimage() # 画像ファイルを読み込む関数を呼び出す
    if e == None: # ウィンドウが閉じられた場合の処理
        break # イベントループを抜ける
win.close() # ウィンドウを閉じる
