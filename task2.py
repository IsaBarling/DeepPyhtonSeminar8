import json

def add_user_to_json_file():
    # Запрашиваем данные у пользователя
    name = input("Введите имя пользователя: ")
    identifier = input("Введите личный идентификатор пользователя: ")
    access_level = input("Введите уровень доступа (от 1 до 7): ")

    # Загружаем существующие данные из файла JSON (если есть)
    try:
        with open('users.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    
    # Проверяем уникальность идентификатора пользователя
    for value in data.values():
        if identifier in value.keys():
            print("Ошибка: пользователь с таким идентификатором уже существует.")
            return
    #return
    # Создаем новую запись пользователя
    user = {
        'name': name,
        'access_level': str(access_level)
    }

    # Добавляем новую запись в соответствующую группу уровня доступа
     
    
    if access_level not in data:
        data[access_level] = {identifier : user}

    b = data[access_level]
    print(b)
    if identifier not in data[access_level].keys():
        data[access_level][identifier] = {}
    
    data[access_level][identifier] = user

    # Сохраняем данные обратно в файл JSON
    with open('users.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("Данные пользователя успешно добавлены.")

# Вызываем функцию add_user_to_json_file в цикле с проверкой команды прерывания
while True:
    add_user_to_json_file()
    choice = input("Хотите добавить еще пользователя? (y/n): ")
    if choice.lower() != 'y':
        break
