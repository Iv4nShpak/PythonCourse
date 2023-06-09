# Задача №25.
#
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

new_str = input().split()
sl = {}
s = ""
for i in new_str:
    if i not in sl:
        s += f'{i} '
        sl[i] = 1
    else:
        s += f"{i}_{str(sl[i])} "
        sl[i] += 1
print(s.strip())
