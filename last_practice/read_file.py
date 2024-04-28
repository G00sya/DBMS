import csv
import codecs

# Укажите путь к вашему CSV файлу
file_path = 'users(1).csv'

# Укажите нужную кодировку
encoding = 'koi8_r'

# Открываем файл с указанием кодировки
with codecs.open(file_path, 'r', encoding) as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)