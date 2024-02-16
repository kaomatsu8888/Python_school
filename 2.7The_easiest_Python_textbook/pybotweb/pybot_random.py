import random

def choice_command(command): # 選択コマンド
    data = command.split() # スペースで分割
    choiced = random.choice(data[1:]) # ランダムに選択
    response = f"{choiced}が選ばれました。" # 選択を表示
    return response # レスポンスを返す

def dice_command(): # サイコロコマンド
    num = random.randint(1, 7) # 1から6までの乱数7は含まないので範囲は1-6
    response = f"{num}が出ました。" # サイコロの目を表示
    return response # レスポンスを返す
