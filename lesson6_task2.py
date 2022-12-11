# Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

a = ['a', '1', 'b', '2', '3', 'c']
b = []
c = []
for i in a:
    if i.isdigit():
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)

# # Решение от преподавателя:
# a = ('a', '1', 'b', '2', '3', 'c')
# b = ('a', 'b', 'c')
# c = ('1', '2', '3')
# b = filter(str.isalpha, a)
# c = filter(str.isdigit, a)
# print(*b)
# print(*c)
