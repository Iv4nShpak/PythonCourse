# Задача 22:
#
# Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые
# встречаются в обоих наборах. Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

first_list = []
second_list = []

for i in range(n):
    first_list.append(int(input('Введите элемент первого множества: ')))

for i in range(m):
    second_list.append(int(input('Введите элемент второго множества: ')))

result = []

for i in first_list:
    if i in second_list and i not in result:
        result.append(i)
print(result)

# a, b = input().split()
# mn1 = set(input().split())
# mn2 = set(input().split())
# print(mn1 & mn2)
