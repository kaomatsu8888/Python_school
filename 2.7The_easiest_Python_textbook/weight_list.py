weight_list = [75, 88, 100]
total = 0
for weight in weight_list:
    total += weight
    print(weight, "kg")
number_of_weight = len(weight_list) # リストの要素数を取得
average = total / number_of_weight # 平均を計算
print(f"平均体重は{average}kgです") # 平均を表示

