def len_command(command):
    cmd, text = command.split()
    length = len(text)
    response = f"文字列の長さは{length}文字です。"
    return response

def wareki_command(command):
    wareki, year_str = command.split()

while True:
    command = input("pybot> ") # ユーザーの入力を待つ
    response = "" # 空の文字列を作成
    for message in bot_dict: # 辞書のキーを取得
        if message in command: # キーがユーザーの入力に含まれていたら
            response = bot_dict[message] # レスポンスを作成
            break # ループを抜ける
    
    if "和暦" in command:
        response = wareki_command(command)
