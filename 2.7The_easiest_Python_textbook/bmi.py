weight_str = input("体重を入力してください(kg):" ) # 体重を入力
height_str_list = weight_str.split(",") # 入力された文字列をカンマで分割

weight_list = []
for height_str in height_str_list:
    weight = int(height_str) # 入力された文字列を整数に変換
    weight_list.append(weight) # リストに追加(append)
    print(weight, "kg")

height_str = input("身長を入力してください(cm):" )
height = int(height_str) # 入力された文字列を整数に変換

for weight in weight_list:
    bmi = weight / (height/100) ** 2 # BMIを計算
    if bmi >= 25: # BMIが25以上で肥満
        result = "肥満です"
    elif bmi >= 18.5: # BMIが18.5以上で標準
        result = "標準です"
    else: # それ以外は痩せている
        result = "痩せています"
    print(f"身長{height}cm、体重{weight}kgのBMIは{bmi}で、判定結果は{result}") # BMIを表示
