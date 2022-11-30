# Вводятся две строки (каждая с новой строчки).
# Из первой строки выделить все символы с чётными индексами, а из второй - с нечётными.
# Объединить строки через пробел и вывести на экран.

# Sample Input:
# Hello
# Python
# Sample Output:
# Hlo yhn

a = input("Enter first string: ")
b = input("Enter second string: ")
print(a[::2],b[1::2])
