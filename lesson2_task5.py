# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# Для N = 5: 1, -3, 9, -27, 81

a = int(input("Enter an integer N: "))
b = int(input("Enter the power of N: "))
i = 0

for i in range(b):
    print(f'{a ** i}', end = ', ')

# добавить вариант из семинара