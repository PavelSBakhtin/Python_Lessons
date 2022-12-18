# import csv
# import json
# def show_menu() -> int:
#     print("\n" + "=" * 20)
#     print("Выберите необходимое действие")
#     print("1. Найти сотрудника")
#     print("2. Сделать выборку сотрудников по должности")
#     print("3. Сделать выборку сотрудников по зарплате")
#     print("4. Добавить сотрудника")
#     print("5. Удалить сотрудника")
#     print("6. Обновить данные сотрудника")
#     print("7. Экспортировать данные в формате json")
#     print("8. Экспортировать данные в формате cmv")
#     print("9. Закончить работу")
#     return int(input("Введите номер необходимого действия: "))

# def read_csv() -> list:
#     employee = []
#     with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
#         csv_reader = csv.reader(fin)
#         for row in csv_reader:
#             temp = {}
#             temp["id"] = int(row[0])
#             temp["last_name"] = row[1]
#             temp["first_name"] = row[2]
#             temp["position"] = row[3]
#             temp["phone_number"] = row[4]
#             temp["salary"] = float(row[5])
#             employee.append(temp)
#     return employee

# def controller():
#     position = -1
#     while position != 9:
#         position = ui()
#         data = read_db()
#         match position:
#             case 1:
#                 find_worker(data)
#             case 2:
#                 find_worker_by_jtitle(data)
#             case 3:
#                 find_worker_by_salary(data)
#             case 4:
#                 add_worker(data)
#             case 5:
#                 delete_worker(data)
#             case 6:
#                 update_worker_data(data)
#             case 7:
#                 json_export(data)
#             case 8:
#                 cmv_export(data)  
#     else:
#         print("конец работы")
