import tkinter as tk #tkに省略

def dispLabel(): #関数に追加する
    lbl.configure(text="こんにちは") #ラベルの文字を「こんにちは」に変更する

root = tk.Tk()
root.geometry("200x100")  

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command = dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()
