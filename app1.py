#fizzbuzz
# 1. 1から100までの数字を表示するプログラムを書きなさい。
# 2. 3の倍数のときは数字の代わりに「Fizz」と表示するプログラムを書きなさい。
# 3. 5の倍数のときは数字の代わりに「Buzz」と表示するプログラムを書きなさい
# 4. 3と5の倍数のときは数字の代わりに「FizzBuzz」と表示するプログラムを書きなさい。

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)




# 自分で書いたコード

# for i in range(1:101):
#     if i % 3 == 0 or i % 5 == 0
# elif:
#     i % 3 == 0
#     print(Fizz)
# elif:
#     i % 5 == 0
#     print(Buzz)
# else:
#     print()


