# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Enter an integer N: "))
dc = {i: 3 * i + 1 for i in range(1, n + 1)}
## Или так:
# dc = {}
# for i in range(n):
#     dc[i + 1] = 3 * (i + 1) + 1
print(dc)

# dc = {'key': 'value'}
# print(dc)  # {'key': 'value'}
# dc['mynewkey'] = 'mynewvalue'
# print(dc)  # {'key': 'value', 'mynewkey': 'mynewvalue'}
