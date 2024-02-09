open_file = open('point.txt') # ファイルを開く
data = open_file.read() # ファイルを読み込む
open_file.close() # ファイルを閉じる
point_data = data.splitlines() # 改行で分割.splitlines()は改行で分割するメソッド

print(point_data) # ファイルの内容を表示

point_dict = {} # 空の辞書を作成
for line in point_data: # リストから要素を1つずつ取り出す
    student_name, points_str = line.split(':') # カンマで分割
    point_dict[student_name] = points_str # 辞書に追加

score_dict = {} # 空の辞書を作成
for student_name in point_dict: # 生徒名を取得
    points_list = point_dict[student_name].split(',') # カンマで分割
    subject_number = len(points_list) # 科目数を取得
    total = 0 # 合計を初期化
    for point in points_list: # 点数を取得
        total = total + int(point) # 合計を計算
        average = total / subject_number # 平均を計算
        score_dict[student_name] = (total, average, subject_number) # 辞書に追加

evaluation_dict = {} # 空の辞書を作成
for student_name in score_dict: # 生徒名を取得
    score_data = score_dict[student_name] # 点数を取得
    total = score_data[0] # 合計を取得
    average = score_data[1] # 平均を取得
    subject_number = score_data[2] # 科目数を取得

    excellent = subject_number * 100 * 0.8 # 優秀基準を計算
    good = subject_number * 100 * 0.65 # 良好基準を計算
    if total >= excellent: # 優秀基準以上
        evaluation = "Excellent"
    elif total >= good: # 良好基準以上
        evaluation = "Good"
    else: # それ以外
        evaluation = "Bad"
    evaluation_dict[student_name] = evaluation # 辞書に追加


file_name = 'evaluation.txt' # ファイル名を設定
output_file = open(file_name, 'w') # ファイルを開く
for student_name in evaluation_dict: # 生徒名を取得
    score_data = score_dict[student_name] # 点数を取得
    total = score_data[0] # 合計を取得

    evaluation = evaluation_dict[student_name] # 評価を取得

    text = f'[{student_name}] total: {total}, evaluation: {evaluation}\n' # テキストを作成
    output_file.write(text) # ファイルに書き込む

output_file.close() # ファイルを閉じる
print(f'{file_name}に保存しました') # 結果を表示
