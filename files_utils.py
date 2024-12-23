import json
import os
import csv
import codecs

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



def read_csv(file_path, delimiter=';', encoding='windows-1251'):
    """
    Читает данные из CSV-файла.

    :param file_path: Путь к файлу.
    :param delimiter: Разделитель полей в файле (по умолчанию ';').
    :param encoding: Кодировка файла (по умолчанию 'windows-1251').
    :return: Данные, считанные из файла.
    """
    data = []
    with codecs.open(file_path, 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            data.append(row)
    return data

def write_csv(data, file_path, delimiter=';', encoding='windows-1251'):
    """
    Записывает данные в CSV-файл.

    :param data: Данные для записи.
    :param file_path: Путь к файлу.
    :param delimiter: Разделитель полей в файле (по умолчанию ';').
    :param encoding: Кодировка файла (по умолчанию 'windows-1251').
    """
    with codecs.open(file_path, 'w', encoding=encoding) as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)

def append_csv(data, file_path, delimiter=';', encoding='windows-1251'):
    """
    Добавляет данные в существующий CSV-файл.

    :param data: Данные для добавления.
    :param file_path: Путь к файлу.
    :param delimiter: Разделитель полей в файле (по умолчанию ';').
    :param encoding: Кодировка файла (по умолчанию 'windows-1251').
    """
    with codecs.open(file_path, 'a', encoding=encoding) as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)

def read_txt(file_path, encoding='utf-8'):
    """
    Читает данные из текстового файла.

    :param file_path: Путь к файлу.
    :param encoding: Кодировка файла (по умолчанию 'utf-8').
    :return: Содержимое файла.
    """
    with codecs.open(file_path, 'r', encoding=encoding) as file:
        content = file.read()
    return content

def write_txt(data, file_path, encoding='utf-8'):
    """
    Записывает данные в текстовый файл.

    :param data: Данные для записи.
    :param file_path: Путь к файлу.
    :param encoding: Кодировка файла (по умолчанию 'utf-8').
    """
    with codecs.open(file_path, 'w', encoding=encoding) as file:
        file.write(data)

def append_txt(data, file_path, encoding='utf-8'):
    """
    Добавляет данные в конец текстового файла.

    :param data: Данные для добавления.
    :param file_path: Путь к файлу.
    :param encoding: Кодировка файла (по умолчанию 'utf-8').
    """
    with codecs.open(file_path, 'a', encoding=encoding) as file:
        file.write(data)

import yaml

def read_yaml(file_path):
    """
    Читает данные из YAML-файла.

    :param file_path: Путь к файлу.
    :return: Данные, считанные из файла.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data
