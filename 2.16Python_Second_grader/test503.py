from pathlib import Path

def savetext(filename): # ファイルにテキストを書き出す
    p = Path(filename) # ファイル名を指定してPathオブジェクトを作る
    txt = "書き出しテスト用テキストデータです。" # 書き出すテキストデータ
    p.write_text(txt, encoding="UTF-8") # ファイルにテキストを書き出す

savetext("output.txt")      # ファイルにテキストを書き出す
 