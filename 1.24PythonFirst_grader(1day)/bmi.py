h = float(input("身長何cmですか？")) / 100.0
w = float(input("体重何kgですか？"))
bmi = w / (h * h) #BMI値を計算
print(f"あなたのBMI値は、{bmi}です")#f記法自分で勉強したやつ楽だよね
print("あなたのBMI値は、",bmi," です。")#これが授業で習ったやつ
print("あなたのBMI値は、bmiです。")#これは表示されないよ
input()
