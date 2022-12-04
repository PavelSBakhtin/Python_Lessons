# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

# Первое решение:
s = input()
with open('lesson4_task1_file.txt', 'a') as data:
    while (len(s) > 0):
        data.write(s + "\n")
        s = input()

# # Другое решение:
# s = input()
# data = open('lesson4_task1_file.txt', 'a')
# while (len(s) > 0):
#     data.write(s + '\n')
#     s = input()
# data.close
