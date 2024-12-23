import json
import os

def read_json(file_path: str, encoding: str = "utf-8"):
    # Читает данные из JSON-файла.
    with open(file_path, 'r', encoding=encoding) as file:
        data = json.load(file)
    return data

def write_json(data, file_path: str, encoding: str = "utf-8"):
    # Записывает данные в JSON-файл.
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def append_json(data: list[dict], file_path: str, encoding: str = "utf-8"):
    # Открываем файл в режиме добавления
    with open(file_path, 'a', encoding=encoding) as file:
        # Преобразуем данные в JSON и добавляем в файл
        json.dump(data, file)
        # Добавляем новую строку для разделения записей
        file.write('\n')
