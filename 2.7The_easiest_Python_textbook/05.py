point_dict = {
    '001': [100, 88, 81],
    '002': [77, 94, 85],
    '003': [80, 52, 99],
}
for student_id in point_dict: # 生徒番号を取得
    points = point_dict[student_id] # 点数を取得
    subject_number = len(points) # 科目数を取得
    japanese, english, math = points # 点数を取得
    total = japanese + english + math # 合計を計算

    excellent = subject_number * 100 * 0.8 # 優秀基準を計算
    good = subject_number * 100 * 0.65 # 良好基準を計算
    if total >= excellent: # 優秀基準以上
        evaluation = "Excellent"
    elif total >= good: # 良好基準以上
        evaluation = "Good"
    else: # それ以外
        evaluation = "Bad"
    print(f"学籍番号{student_id}の合計点は{total}で、評価は{evaluation}です") # 結果を表示
