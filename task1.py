import json

def create_json_file(source, result_file):
    # Читаем данные из входного файла
    with open(source, 'r') as file:
        lines = file.readlines()

    data = []
    # Обрабатываем каждую строку
    for line in lines:
        # Разделяем строку на имя и произведение
        name, result = line.strip().split('|')
        # Преобразуем имя в формат с большой буквы
        name = name.capitalize()
        # Создаем словарь с данными
        entry = {
            'name': name,
            'result': float(result)
        }
        # Добавляем словарь в список
        data.append(entry)

    # Сериализуем данные в формат JSON и записываем в выходной файл
    with open(result_file, 'w') as file:
        json.dump(data, file, indent=4)

    print("Результаты сохранены в файл:", result_file)

# Вызываем функцию create_json_file с указанием входного и выходного файлов
create_json_file('output.txt', 'output.json')
