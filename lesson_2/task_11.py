# Задача №11
#
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6


input_num = int(input('Введите число: '))

n1, n2 = 0, 1   # 0 1 1 2 3 5 8
f_id = 2
while n2 < input_num:
    n1, n2 = n2, n1 + n2
    f_id += 1
if input_num != n2:
    f_id = -1
print(f_id)
