import datetime

now = datetime.datetime.now()
print(f"{now:%H時:%M分:%S秒}")
print(f"{now:%Y年%m月%d日}")
print(f"{now:%Y年%m月%d日 %H時:%M分:%S秒}")
# 表記を変える
print(f"{now:%Y/%m/%d %H:%M:%S}")
print(f"{now:%p %I時:%M分:%S秒}")

