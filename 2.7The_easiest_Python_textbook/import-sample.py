from calc import add, sub # calcファイルからadd関数とsub関数をimportする
from calc import add as a, sub as s # calcファイルからadd関数をaとして、sub関数をsとしてimportする

sum = add(1, 2) # add関数を使って1と2を足す
diff = sub(5, 3) # sub関数を使って5から3を引く
print(sum, diff) # 足し算と引き算の結果を表示
