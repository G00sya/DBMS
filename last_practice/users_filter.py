import csv
import codecs

file_path = 'users(1).csv'
output_file_path = 'clear_users.csv'
encoding = 'koi8_r'
arr = []

# Открываем файл с указанием кодировки
with codecs.open(file_path, 'r', encoding) as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        arr.append(row)

with open(output_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['info'])
    for row in arr:
        # Создаем словарь, объединяя именованные поля с каждым значением в строке
        row_dict = {field: value for field, value in zip(writer.fieldnames, row)}
        writer.writerow(row_dict)