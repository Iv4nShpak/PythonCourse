# ЗАДАЧА №2
#
#Найдите сумму цифр трехзначного числа.
#
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Вариант 1
num = input("Введите трехзначное число: ")
a = int(num[0])
b = int(num[1])
c = int(num[2])
print(f"Сумма трехзначного числа: {a + b + c}")

# Вариант 2
z = 0
for i in num:
    z += int(i)
print(f"Сумма трехзначного числа: {z}")

