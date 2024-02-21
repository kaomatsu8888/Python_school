# ストップウォッチ

# import time

# print('Enterを押すとスタートします。')
# input()
# start = time.time()
# print('ストップウォッチスタート')
# print('Enterを押すとストップします。')
# input()
# end = time.time()
# print('ストップウォッチストップ')
# print(f'経過時間: {end - start}秒')

# # このプログラムは、Enterを押すとスタートし、再度Enterを押すとストップするストップウォッチです。
# # timeモジュールのtime関数を使って、現在の時間を取得しています。


import datetime

start = datetime.datetime.now()
input = ("Enterを押すとスタートします。")
now = datetime.datetime.now()
td = now - start
print(td)

