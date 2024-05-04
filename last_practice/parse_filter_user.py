import csv
import re

# Функция для извлечения user_id, email и city из строки
def parse_data(data):
    # Опять немного магии с регулярными выражениями
    match = re.match(r'User_(\d+)\t(.*?)@(\S+?)\.(\S+)\s+(.*)', data)
    if match:
        user_id = match.group(1)
        email = match.group(2) + '@' + match.group(3) + '.' + match.group(4)
        city = match.group(5).strip()
        return user_id, email, city
    return None, None, None

# Открываю исходный csv-шник для чтения и создаю распаршеный csv-шник
with open('clear_users.csv', 'r') as csv_file, open('clear_users_parsed.csv', 'w', newline='') as output_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(output_file)
    # Обрабатываю каждую строку исходного файла
    for row in csv_reader:
        data = row[0]
        parsed_data = parse_data(data)
        if all([parsed_data[i] is not None and parsed_data[i] != "" for i in range(len(parsed_data))]):
            # Записываю распаршенные данные в новый файл
            csv_writer.writerow([parsed_data[0], parsed_data[1], parsed_data[2]])