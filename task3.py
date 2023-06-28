import json
import csv

def save_json_to_csv(input_file, output_file):
    # Загружаем данные из файла JSON
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Открываем файл CSV для записи
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Записываем заголовки столбцов
        writer.writerow(['ID','Name', 'Access Level'])

        # Записываем данные в CSV
        for access_level, users in data.items():
            for user_id, user_data in users.items():
                writer.writerow([user_id, user_data['name'], user_data['access_level']])

    print("Данные успешно сохранены в файле:", output_file)

# Вызываем функцию save_json_to_csv с указанием входного и выходного файлов
save_json_to_csv(r'users.json', 'users.csv')
