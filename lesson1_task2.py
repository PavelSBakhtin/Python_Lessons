# Задача 2.
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
d = int(input('Enter the fourth number: '))
e = int(input('Enter the fifth number: '))

lst = [a, b, c, d, e]
print(lst)
max = lst[0]
for i in lst:
    if max < i:
        max = i
print('max number is: ', max)
