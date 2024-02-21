import PySimpleGUI as sg

loadname = sg.popup_get_file("テキストファイルを選択してください。") # ファイル選択ダイアログを表示する。
print(loadname) # 選択したファイルのパスを表示する。
