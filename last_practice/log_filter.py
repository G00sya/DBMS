import csv
import codecs
import re

# Указываю параметры для дальнейшей работы с файлами
file_path = 'log(1).csv'
output_file_path = 'clear_log.csv'
encoding = 'utf-8'

# Функция для парсинга данных
def extract_values(data):
    # Использую немного регулярных выражений для обработки
    user_id_ = re.search(r'user_(\d+)', data[0])
    user_id = user_id_.group(1) if user_id_ else None

    date_ = data[1].strip('[') if len(data) > 1 else None
    time = date_.split(' ')[1] if date_ else None
    date = date_.split(' ')[0] if date_ else None
    date_time = None
    if date and time:
        date_time = date + " " + time

    bet = data[2] if len(data) > 2 else None
    win = data[3] if len(data) > 3 else None
    return {'user_id': user_id, 'date_time': date_time,'bet': bet, 'win': win}

# Массив с отфильтрованными данными
filtered_arr = []

# Читаем данные из первого csv-шника
with codecs.open(file_path, 'r', encoding) as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        flag = True
        filtered_data = extract_values(row)
        for elem in filtered_data.values():
            if elem is None:
                flag = False
        if flag:
            filtered_arr.append(filtered_data)

# Записываем данные в другой csv-шник
with open(output_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['user_id', 'date_time', 'bet', 'win'])
    for data in filtered_arr:
        writer.writerow(data)
