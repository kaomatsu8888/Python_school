# データの種類
#i = 100 # 整数型
#f = 12.3 #浮動小数点型
#w = "hello" #文字数型
#b = True #ブール型
#print(i, f, w, b)

# 文字列をつなぐ
#w ="こんにちは。" + "私はパイソンです。"
#print(w)

# 文字数を調べる
#w ="こんにちは。" + "私はパイソンです。"
#print(len(w))

# 文字列を取り出す
#w ="こんにちは。" + "私はパイソンです。"
#print(w[0]) #一つだけ
#print(w[6:12])
#print(w[-3:])
#print(w[0:5])

# 文字列の途中で改行するには？
#w = "こんにちは。" + "\n" + "私はパイソンです"
#print(w)

#データ型を変換する
#a = "100"
#print(a+23)

# テスト２
#a = "100"
#b = "こんにちは"
#print(a.isdigit())
#print(b.isdigit())

##
##b = "こんにちは"
##if b.isdigit():
##    print(int(b)+23)
##else:
##    print("数値じゃないよ")


lunch = ["おにぎり","パスタ","ハンバーガー","カレー","定食"]
print(lunch[2])
input()

##score = 79
##if score > 80:
##    print("やったね！")
##    print("次もこの調子だ")
##else:
##        print("残念でした")

for i in range(10):
    print(5,"✕",i,"=",5*i)
input()

scorelist = [64,100,78,80,72]
for i in scorelist:
    print(i)
input()
