import os
import json
import pickle

def json_to_pickle(directory):
    # Получаем список всех файлов в директории
    files = os.listdir(directory)
    
    # Фильтруем список файлов, оставляя только файлы JSON
    json_files = [file for file in files if file.endswith('.json')]

    for json_file in json_files:
        # Создаем путь к файлу JSON
        json_path = os.path.join(directory, json_file)
        
        # Читаем файл JSON
        with open(json_path, 'r') as jf:
            data = json.load(jf)
        
        # Создаем путь к файлу pickle
        pickle_file = json_file[:-5] + '.pickle'
        pickle_path = os.path.join(directory, pickle_file)
        
        # Записываем данные в файл pickle
        with open(pickle_path, 'wb') as pf:
            pickle.dump(data, pf)

# Путь к директории, которую нужно сканировать
directory = '.\\'
json_to_pickle(directory)
print("finish")
