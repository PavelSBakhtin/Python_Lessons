# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример: Для N = 5: 1, -3, 9, -27, 81

a = -3
b = int(input("Enter the power of N: "))
i = 0

print(f'Для N = {b}: ')
for i in range(b - 1):
    print(f'{a ** i}', end = ', ')
print(a ** (b - 1))
