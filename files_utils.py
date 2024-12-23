import json

def read_json(file_path: str, encoding: str = "utf-8"):
    """Читает данные из JSON-файла."""
    with open(file_path, 'r', encoding=encoding) as file:
        data = json.load(file)
    return data

def write_json(data, file_path: str, encoding: str = "utf-8"):
    """Записывает данные в JSON-файл."""
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)