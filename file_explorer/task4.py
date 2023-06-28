#import csv
import json
import hashlib

def process_csv_to_json(input_file, output_file):
    # Читаем CSV файл
    with open(input_file, 'r') as file:
        #reader = csv.reader(file)
        reader = [line.rstrip() for line in file]
        #print(reader)
        # Создаем список для хранения записей в формате JSON
        records = []

        # Обрабатываем каждую строку CSV
        n = 0
        for line in reader:
            if n == 0:
                n+=1
                continue
            row = line.split(',')
            
            name = row[1]
            access_level = row[2]

            # Дополняем id нулями до 10 цифр
            user_id = row[0].zfill(10)
            #или
            user_id = "0" * (10-len(row[0])) + row[0]
            

            # Преобразуем первую букву имени в прописную
            name = name.capitalize()
            #или
            name = name[0].upper() + name[1:]
            # Вычисляем хеш на основе имени и идентификатора
            hash_value = hashlib.sha256((name + user_id).encode()).hexdigest()

            # Создаем словарь с данными и добавляем его в список записей
            record = {
                'name': name,
                'access_level': access_level,
                'user_id': user_id,
                'hash': hash_value
            }
            records.append(record)

    # Сохраняем записи в JSON файле
    with open(output_file, 'w') as file:
        json.dump(records, file, indent=4)

    print("Данные успешно сохранены в файле:", output_file)

# Вызываем функцию process_csv_to_json с указанием входного и выходного файлов
process_csv_to_json('users.csv', 'users_processed2.json')
