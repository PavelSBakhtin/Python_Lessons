# В текстовом файле посчитать количество строк, а также для каждой отдельной
# строки определить количество в ней символов и слов.

path = 'lesson4_file.txt'
data = open(path, 'r')
count = 0
for i in data.readlines():
    print(i, end = "")
    print(f"Number of characters = {len(i)}")
    print(f"Number of words = {len(i.split())}" + '\n')
    count += 1
data.close()
print(f"Number of lines: {count}")
