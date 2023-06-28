import pickle
import csv

def pickle_to_csv(pickle_file, csv_file):
    # Читаем данные из pickle файла
    with open(pickle_file, 'rb') as pf:
        data = pickle.load(pf)
        
    # Проверяем, что данные не пусты
    if data:
        # Получаем заголовки для CSV файла
        headers = data[0].keys()

        # Записываем данные в CSV файл
        with open(csv_file, 'w', newline='') as cf:
            writer = csv.DictWriter(cf, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    else:
        print(f"Pickle file {pickle_file} is empty")
        
# Пример использования
pickle_file = "output.pickle"
csv_file = 'outputFromPickle.csv'
pickle_to_csv(pickle_file, csv_file)
