# import re
# st = "4, 6. 8"
# print(re.split(".,", st))

# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr".
# То есть, функция должна возвращать True, если такой фрагмент присутствует в строке
# и False - в противном случае.

print((lambda x: 'plr' in x)(input()))

# НОД

import random
a = random.randint(33, 99)
b = random.randint(33, 99)
c = [a, b]
print(c)
while max(a, b) % min(a, b) != 0:
    if a > b:
        a = a % b
    elif a < b:
        b = b % a
print(min(a, b))
