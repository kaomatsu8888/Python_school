from pathlib import Path
import chardet  

def loadtext(filename): # ファイルからテキストを読み込む
    with open(filename, "rb") as f: # バイナリモードでファイルを開く
        b = f.read() # ファイルからバイト列を読み込む
        enc = chardet.detect(b)["encoding"] # 文字コードを自動判別する
        p = Path(filename) # ファイル名を指定してPathオブジェクトを作る
        txt = p.read_text(encoding = enc) # ファイルからテキストを読み込む
        print(f"{filename} : {txt}") # 読み込んだテキストを表示
loadtext("utest.txt")  # ファイルからテキストを読み込む
loadtext("stest.txt")  # ファイルからテキストを読み込む
