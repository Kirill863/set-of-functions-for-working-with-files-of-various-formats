import json
import csv
import yaml
import codecs

# Создание тестового файла test.txt
txt_data = "Hello, World!\n"
with codecs.open('test.txt', 'w', encoding='utf-8') as file:
    file.write(txt_data)

# Создание тестового файла test.json
json_data = {
    "name": "Ivan Ivanov",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "Anystate",
    }
}
with open('test.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

# Создание тестового файла test.csv
csv_data = [
    ["name", "age", "city"],
    ["John Doe", "30", "Anytown"],
    ["Jane Smith", "25", "Othertown"]
]
with codecs.open('test.csv', 'w', encoding='windows-1251') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(csv_data)

# Создание тестового файла test.yaml
yaml_data = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "Anystate",
        "zip": "12345"
    }
}
with open('test.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(yaml_data, file)
