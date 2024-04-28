import csv
import codecs
import re

file_path = 'log(1).csv'
output_file_path = 'clear_log.csv'
encoding = 'utf-8'

def extract_values(data):
    user_id_ = re.search(r'user_(\d+)', data[0])
    user_id = user_id_.group(1) if user_id_ else None

    date_ = data[1].strip('[') if len(data) > 1 else None
    time = date_.split(' ')[1] if date_ else None
    bet = data[2] if len(data) > 2 else None
    win = data[3] if len(data) > 3 else None
    return {'user_id': user_id, 'date': time,'bet': bet, 'win': win}

filtered_arr = []

with codecs.open(file_path, 'r', encoding) as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        filtered_data = extract_values(row)
        filtered_arr.append(filtered_data)  # Добавляем отдельные данные, а не весь список

with open(output_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['user_id', 'date', 'bet', 'win'])
    #writer.writeheader()
    for data in filtered_arr:
        writer.writerow(data)
