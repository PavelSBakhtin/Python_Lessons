# Задача 4.
# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

N = float(input("Enter any number: "))

N = abs(N)
N = (N - N // 1)
if N==0:
    print("no")
else:
    N = N * 10
    N = N // 1
    print(int(N))

# if N % 1 != 0:
#     print(int(N % 1 * 10))
# else:
#     print("no")
