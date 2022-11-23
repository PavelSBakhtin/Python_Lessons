# Задача 3.
# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N.

N = int(input("Enter any number: "))
lst = []
for i in range(-N, N+1):
  print(i, end = " ")
