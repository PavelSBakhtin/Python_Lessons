# Задача 1.
# Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))

if x**2 == y or y**2 == x:
    print('yes')
else:
    print('no')
