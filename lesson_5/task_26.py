# Задача 26:
#
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую
# степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def degree_of_number(A, B):
    if B == 0:
        return 1
    else:
        return A * degree_of_number(A, B - 1)

print(degree_of_number(3, 5))
print(degree_of_number(2, 3))