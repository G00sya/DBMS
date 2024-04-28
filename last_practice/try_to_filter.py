import csv
import re

# Функция для извлечения user_id, email и city из строки
def parse_data(data):
    match = re.match(r'User_(\d+)(.*?)@(\S+?)\.(\S+)\s+(.*)', data)
    if match:
        user_id = match.group(1)
        email = match.group(2) + '@' + match.group(3) + '.' + match.group(4)
        city = match.group(5).strip()
        return user_id, email, city
    return None, None, None

# Открываем исходный CSV файл для чтения и создаем новый CSV файл для записи
with open('clear_users.csv', 'r') as csv_file, open('clear_users_parsed.csv', 'w', newline='') as output_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(output_file)

    # Записываем заголовки в новый файл
    csv_writer.writerow(['user_id', 'email', 'city'])

    # Обрабатываем каждую строку исходного файла
    for row in csv_reader:
        data = row[0]
        user_id, email, city = parse_data(data)

        # Записываем распарсенные данные в новый файл
        csv_writer.writerow([user_id, email, city])