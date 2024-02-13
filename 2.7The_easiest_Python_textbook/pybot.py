command_file = open('pybot.txt', encoding='utf-8')
raw_data = command_file.read() # ファイルを読み込む
command_file.close() # ファイルを閉じる
lines = raw_data.splitlines() # 改行で分割

bot_dict = {} # 空の辞書を作成
for line in lines:
    word_list = line.split(',') # カンマで分割
    key = word_list[0] # 最初の要素をキーに
    response = word_list[1] # 2番目の要素を値に
    bot_dict[key] = response # ディクショナリに追加

while True:
    command = input("pybot> ") # ユーザーの入力を待つ
    response = "" # 空の文字列を作成
    for message in bot_dict: # 辞書のキーを取得
        if message in command: # キーがユーザーの入力に含まれていたら
            response = bot_dict[message] # レスポンスを作成
            break
        if "和暦" in command:
            wareki, year_str = command.split()
            year = int(year_str)        
            if year >= 2019:
                reiwa = year - 2018
                response = f"西暦{year}年は、令和{reiwa}年です。"
            elif year >= 1989:
                heisei = year - 1988
                response = f"西暦{year}年は、平成{heisei}年です。"
            else:
                response = f"西暦{year}年ハ、平成より前です。"
                break

    if not response: # レスポンスが空のままなら
        response = "何言ってるかわかんない"
    print(response) # レスポンスを表示

    if "さようなら" in command:
        break



