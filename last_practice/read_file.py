import csv
import codecs

# Путь до моего csv-шника
file_path = 'users(1).csv'

# Указываю кодировку
encoding = 'koi8_r'

# Открываю файл для чтения
with codecs.open(file_path, 'r', encoding) as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)