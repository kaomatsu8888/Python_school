year_str = input("あなたの生まれてきた西暦4桁を入力してください:")
year = int(year_str) # 入力された文字列を整数に変換
number_of_eto = (year + 8) % 12 # 干支の計算.8を足して12で割った余りが干支.1988年は(1988 + 8) % 12 = 166あまり4
print(number_of_eto) # 干支を表示
eto_tuple = ("子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥") # 干支のタプル()だったらタプルだよ！！
eto_name = eto_tuple[number_of_eto] # 干支のタプルから干支の名前を取得
print(year, "あなたのの干支の順番は", number_of_eto, "番です。", eto_name, "です。") # 干支を表示19
