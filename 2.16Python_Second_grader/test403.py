import datetime

now = datetime.datetime.now()
print(f"現在 = {now:%H時:%M分:%S秒}")
goal = now.replace(hour=20, minute=30, second=0)
print(f"目標 = {goal:%H時:%M分:%S秒}")
td = goal - now
print(td)
