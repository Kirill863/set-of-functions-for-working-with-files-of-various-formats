import json

def read_json(file_path: str, encoding: str = "utf-8"):
    """Читает данные из JSON-файла."""
    with open(file_path, 'r', encoding=encoding) as file:
        data = json.load(file)
    return data

