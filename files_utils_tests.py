import os
import json
import csv
import yaml
from files_utils import (
    read_json, write_json, append_json,
    read_csv, write_csv, append_csv,
    read_txt, write_txt, append_txt,
    read_yaml
)

def test_read_json():
    file_path = 'test.json'
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    expected_data = {
        "name": "John Doe",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "Anystate",
            "zip": "12345"
        }
    }
    try:
        content = read_json(file_path)
        assert content == expected_data, f"Expected {expected_data}, but got {content}"
        print("test_read_json passed")
    except Exception as e:
        print(f"test_read_json failed: {e}")

def test_write_json():
    file_path = 'test_write.json'
    test_data = {"name": "Jane Smith", "age": 25}
    write_json(test_data, file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = json.load(file)
    assert content == test_data, f"Expected {test_data}, but got {content}"
    os.remove(file_path)
    print("test_write_json passed")

def test_append_json():
    file_path = 'test_append.json'
    initial_data = [{"name": "John Doe", "age": 30}]
    additional_data = [{"name": "Jane Smith", "age": 25}]
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(initial_data, file)

    append_json(additional_data, file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = json.load(file)
    expected_content = initial_data + additional_data
    assert content == expected_content, f"Expected {expected_content}, but got {content}"
    os.remove(file_path)
    print("test_append_json passed")

def test_read_csv():
    file_path = 'test.csv'
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    expected_data = [
        ["name", "age", "city"],
        ["John Doe", "30", "Anytown"],
        ["Jane Smith", "25", "Othertown"]
    ]
    content = read_csv(file_path)
    assert content == expected_data, f"Expected {expected_data}, but got {content}"
    print("test_read_csv passed")

def test_write_csv():
    file_path = 'test_write.csv'
    test_data = [
        ["name", "age", "city"],
        ["Alice Johnson", "28", "Somewhere"]
    ]
    write_csv(test_data, file_path)

    with open(file_path, 'r', encoding='windows-1251') as file:
        reader = csv.reader(file, delimiter=';')
        content = list(reader)
    assert content == test_data, f"Expected {test_data}, but got {content}"
    os.remove(file_path)
    print("test_write_csv passed")

def test_append_csv():
    file_path = 'test_append.csv'
    initial_data = [
        ["name", "age", "city"],
        ["John Doe", "30", "Anytown"]
    ]
    additional_data = [
        ["Jane Smith", "25", "Othertown"]
    ]

    # Записываем начальные данные в файл
    with open(file_path, 'w', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(initial_data)

    # Добавляем дополнительные данные в файл
    with open(file_path, 'a', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(additional_data)

    # Читаем содержимое файла для проверки
    with open(file_path, 'r', encoding='windows-1251') as file:
        reader = csv.reader(file, delimiter=';')
        content = list(reader)

    expected_content = initial_data + additional_data
    assert content == expected_content, f"Expected {expected_content}, but got {content}"
    os.remove(file_path)
    print("test_append_csv passed")

def test_read_txt():
    file_path = 'test.txt'
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    expected_data = "Hello, World!\n"
    content = read_txt(file_path)
    assert content == expected_data, f"Expected {expected_data}, but got {content}"
    print("test_read_txt passed")

def test_write_txt():
    file_path = 'test_write.txt'
    test_data = "This is a test write operation."
    write_txt(test_data, file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    assert content == test_data, f"Expected {test_data}, but got {content}"
    os.remove(file_path)
    print("test_write_txt passed")

def test_append_txt():
    file_path = 'test_append.txt'
    initial_data = "This is the initial data.\n"
    additional_data = "This is the additional data.\n"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(initial_data)

    append_txt(additional_data, file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    assert content == initial_data + additional_data, f"Expected {initial_data + additional_data}, but got {content}"
    os.remove(file_path)
    print("test_append_txt passed")

def test_read_yaml():
    file_path = 'test.yaml'
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    expected_data = {
        "name": "John Doe",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "Anystate",
            "zip": "12345"
        }
    }
    content = read_yaml(file_path)
    assert content == expected_data, f"Expected {expected_data}, but got {content}"
    print("test_read_yaml passed")

if __name__ == "__main__":
    test_read_json()
    test_write_json()
    test_append_json()
    test_read_csv()
    test_write_csv()
    test_append_csv()
    test_read_txt()
    test_write_txt()
    test_append_txt()
    test_read_yaml()
