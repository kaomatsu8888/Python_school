import PySimpleGUI as sg

savename = sg.popup_get_file("名前をつけて保存してください。", 
           default_path = "test.txt", save_as=True) # save_as=Trueは名前をつけて保存ダイアログを表示する。
print(savename)
