#A-1
#"Bob "Tom", "Ken" という3つの文字列要素を持つ
#usersというリストを定義してください。OK

users = ["Bob","Tom","Ken"]
print(users)

# 1から5までの整数を要素として持つint_numbersリストを定義してください

int_numbers = [1,2,3,4,5]
print(int_numbers)
# 別解その1
#int_numbers = list(range(1, 6))

# 別解その2
#int_numbers = [i for i in range(1, 6)]

#"Bob", "Dylan", 79 という 3つの要素をもつbob_infoという
#リストを定義してください OK

bob_info = {"Bob","Dylan",79}
print(bob_info)

#次のmembersというリストから "Bob" と "Tom" を取得して出力してください
members = ["Bob", "Tom", "Ken"]
stamen = members[0:2]
print(stamen)

#次のリストを利用して、"Name: Bob Dylan, Age: 79"と出力してください
bob_info = ["Bob", "Dylan", 79]
print(bob_info)

#for を使って odd_numbers の各要素を出力してください
# 見ないで書いたやつ↓
#odd_numbers = [1, 3, 5, 7, 9]
#    for number in odd_numbers

# 参考書をみて考えたやつ
odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
        print(i)

##odd_numbers = [1, 3, 5, 7, 9]
##
##for number in odd_numbers:
##    print(number)

#for を使って even_numbers のそれぞれの値を2倍した値を出力してください
        #できませんでした
even_numbers = [2, 4, 6, 8]
for i in even_numbers:
    for j in 2:#コンマ忘れた
        print(i*j)

#正解のやつ
##even_numbers = [2, 4, 6, 8]
##
##for number in even_numbers:
##    print(number * 2)




# users_info を使って次のような出力をしてください
##Name: Bob, Age: 79
##Name: Tom, Age: 59
##Name: Ken, Age: 61
##users_info = [["Bob", 79],
##              ["Tom", 59],
##              ["Ken", 61]]

import random

dice =[1,2,3,4,5,6]
print(random.choice(dice))

