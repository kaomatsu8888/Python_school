def wareki_command(command): # 和暦コマンド
    wareki, year_str = command.split() # 和暦と年に分ける
    year = int(year_str)         # 年を整数に変換
    if year >= 2019:            # 2019年以降は
        reiwa = year - 2018    # 2018を引く
        response = f"西暦{year}年は、令和{reiwa}年です。" # 令和を表示
    elif year >= 1989:       # 1989年以降は
        heisei = year - 1988 # 1988を引く
        response = f"西暦{year}年は、平成{heisei}年です。" # 平成を表示
    else:                       # それ以外は
        response = f"西暦{year}年ハ、平成より前です。" # 平成以前を表示
    return response            # レスポンスを返す

command_file = open('pybot.txt', encoding='utf-8') # ファイルを開く


