year_str = input("あなたの生まれてきた西暦4桁を入力してください:")
year = int(year_str)
number_of_eto = (year + 8) % 12
print(year, "あなたのの干支の順番は", number_of_eto, "番です。")
