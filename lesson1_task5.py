# Задача 5.
# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

N = int(input("Enter any number: "))
if (N % 5 == 0 and N % 10 == 0 or N % 15 == 0) and N % 30 != 0:
    print("multiples")
else:
    print("repeatedly")
