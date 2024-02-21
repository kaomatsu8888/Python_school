import PySimpleGUI as sg
import datetime

layout = [[sg.T(font=("Arial",40), k="txt",
          size=(20,1), justification="center")]] # justificationは文字列の位置を指定する。centerは中央に表示する。
win = sg.Window("時計テスト", layout, size=(320,80), keep_on_top=True) # keep_on_top=Trueは常に最前面に表示する。
c = 0
while True:
    e, v = win.read(timeout=500) # timeout=500は500ミリ秒ごとにイベントを取得する。
    c = c + 1
    win["txt"].update(f"{c}") # update()は指定したキーの値を更新する。
    if e == None:
        break
win.close() # close()はウィンドウを閉じる。
